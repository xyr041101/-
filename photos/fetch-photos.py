#!/usr/bin/env python3
"""Pexels 批量图片下载器（仅用标准库，无第三方依赖）。

用法：
    python fetch-photos.py --help
    python fetch-photos.py --per-keyword 30
    python fetch-photos.py --keywords "机械臂,控制柜" --per-keyword 20 --orientation landscape

需要环境变量 PEXELS_API_KEY（免费申请：https://www.pexels.com/api/）。
"""

import argparse
import json
import os
import sys
import time
import urllib.parse
import urllib.request

DEFAULT_KEYWORDS = [
    "机械臂", "自动化产线", "控制柜", "PLC", "传感器", "电池模组",
    "车间", "仓储物流", "伺服电机", "工业相机", "洁净车间", "设备维护",
]

API = "https://api.pexels.com/v1/search"


def build_headers(api_key):
    return {"Authorization": api_key, "User-Agent": "design-kit-photo-fetcher"}


def fetch_one_page(keyword, page, per_page, orientation, min_width, api_key):
    params = {
        "query": keyword,
        "per_page": str(min(per_page, 80)),
        "page": str(page),
    }
    if orientation:
        params["orientation"] = orientation
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers=build_headers(api_key))
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def safe_name(text, limit=40):
    keep = []
    for ch in text:
        if ch.isalnum() or ch in "-_":
            keep.append(ch)
    return ("".join(keep)[:limit] or "keyword")


def download(url, dest):
    req = urllib.request.Request(url, headers={"User-Agent": "design-kit-photo-fetcher"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = resp.read()
    with open(dest, "wb") as f:
        f.write(data)
    return len(data)


def run(args):
    api_key = os.environ.get("PEXELS_API_KEY", "").strip()
    if not api_key:
        print("缺少环境变量 PEXELS_API_KEY。申请：https://www.pexels.com/api/", file=sys.stderr)
        return 2

    keywords = (
        [k.strip() for k in args.keywords.split(",") if k.strip()]
        if args.keywords
        else DEFAULT_KEYWORDS
    )

    total_saved = 0
    for kw in keywords:
        folder = os.path.join(args.out, safe_name(kw))
        os.makedirs(folder, exist_ok=True)
        saved, page = 0, 1
        while saved < args.per_keyword:
            need = min(args.per_keyword - saved, 80)
            try:
                data = fetch_one_page(kw, page, need, args.orientation, args.min_width, api_key)
            except Exception as exc:  # 单个关键词失败不影响其它
                print(f"[{kw}] 请求失败: {exc}", file=sys.stderr)
                break
            photos = data.get("photos", [])
            if not photos:
                break
            for p in photos:
                if saved >= args.per_keyword:
                    break
                width = p.get("width", 0)
                if width and width < args.min_width:
                    continue
                src = p.get("src", {})
                url = src.get("large2x") or src.get("large") or src.get("original")
                if not url:
                    continue
                dest = os.path.join(folder, f"{p.get('id')}.jpg")
                if os.path.exists(dest):
                    continue
                try:
                    size = download(url, dest)
                except Exception as exc:
                    print(f"[{kw}] 下载失败 {p.get('id')}: {exc}", file=sys.stderr)
                    continue
                saved += 1
                total_saved += 1
                print(f"[{kw}] {saved}/{args.per_keyword} -> {dest} ({size // 1024} KB)")
            page += 1
            if page > 20:
                break
            time.sleep(0.5)

    print(f"\n完成，共下载 {total_saved} 张，目录：{os.path.abspath(args.out)}")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Pexels 批量图片下载器")
    parser.add_argument("--keywords", help="逗号分隔的关键词，默认用内置工业类词表")
    parser.add_argument("--per-keyword", type=int, default=30, help="每个关键词下载张数，默认 30")
    parser.add_argument("--orientation", choices=["landscape", "portrait", "square"], help="图片方向")
    parser.add_argument("--min-width", type=int, default=1200, help="最小宽度，默认 1200")
    parser.add_argument("--out", default="photos/raw", help="输出目录，默认 photos/raw")
    raise SystemExit(run(parser.parse_args()))


if __name__ == "__main__":
    main()
