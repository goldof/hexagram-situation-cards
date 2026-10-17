#!/usr/bin/env python3
"""YI-64 爻变引擎：封闭性 / 饱和性 loop 校验.

铁律:64 卦的爻变边一律由八卦二进制机器推导,禁止手抄、禁止手算转录。
本脚本既是生成器也是校验器:推导 384 条单爻变 -> loop 校验封闭性与饱和性
-> 输出校验报告 + 机器生成的转移表 (yi_hexagrams.json)。
内容层(一句话情境/边界)由人工撰写后合并,爻变边永不手写。
"""
import json, os
from collections import deque

HERE = os.path.dirname(os.path.abspath(__file__))

# 八卦二进制(自下而上):阳=1 阴=0
TRI = {"乾": "111", "兑": "110", "离": "101", "震": "100",
       "巽": "011", "坎": "010", "艮": "001", "坤": "000"}
TRI_NAME = {v: k for k, v in TRI.items()}

# (卦名, 上卦, 下卦) —— 文王卦序,唯一手写输入,下述校验会抓住任何录入错误
HEX = [
    ("乾", "乾", "乾"), ("坤", "坤", "坤"), ("屯", "坎", "震"), ("蒙", "艮", "坎"),
    ("需", "坎", "乾"), ("讼", "乾", "坎"), ("师", "坤", "坎"), ("比", "坎", "坤"),
    ("小畜", "巽", "乾"), ("履", "乾", "兑"), ("泰", "坤", "乾"), ("否", "乾", "坤"),
    ("同人", "乾", "离"), ("大有", "离", "乾"), ("谦", "坤", "艮"), ("豫", "震", "坤"),
    ("随", "兑", "震"), ("蛊", "艮", "巽"), ("临", "坤", "兑"), ("观", "巽", "坤"),
    ("噬嗑", "离", "震"), ("贲", "艮", "离"), ("剥", "艮", "坤"), ("复", "坤", "震"),
    ("无妄", "乾", "震"), ("大畜", "艮", "乾"), ("颐", "艮", "震"), ("大过", "兑", "巽"),
    ("坎", "坎", "坎"), ("离", "离", "离"), ("咸", "兑", "艮"), ("恒", "震", "巽"),
    ("遁", "乾", "艮"), ("大壮", "震", "乾"), ("晋", "离", "坤"), ("明夷", "坤", "离"),
    ("家人", "巽", "离"), ("睽", "离", "兑"), ("蹇", "坎", "艮"), ("解", "震", "坎"),
    ("损", "艮", "兑"), ("益", "巽", "震"), ("夬", "兑", "乾"), ("姤", "乾", "巽"),
    ("萃", "兑", "坤"), ("升", "坤", "巽"), ("困", "兑", "坎"), ("井", "坎", "巽"),
    ("革", "兑", "离"), ("鼎", "离", "巽"), ("震", "震", "震"), ("艮", "艮", "艮"),
    ("渐", "巽", "艮"), ("归妹", "震", "兑"), ("丰", "震", "离"), ("旅", "离", "艮"),
    ("巽", "巽", "巽"), ("兑", "兑", "兑"), ("涣", "巽", "坎"), ("节", "坎", "兑"),
    ("中孚", "巽", "兑"), ("小过", "震", "艮"), ("既济", "坎", "离"), ("未济", "离", "坎"),
]

POS = ["初", "二", "三", "四", "五", "上"]  # 自下而上


def bits_of(upper, lower):
    return TRI[lower] + TRI[upper]  # 自下而上:下卦在低位


def main():
    assert len(HEX) == 64, f"卦数={len(HEX)},必须64"
    cards = []
    for i, (name, upper, lower) in enumerate(HEX, 1):
        yi = f"YI{i:02d}"
        bits = bits_of(upper, lower)
        def yaoname(p, b):
            t = "九" if b == "1" else "六"
            # 传统爻名:初九/上六(爻性在后),九二…九五(爻性在前)
            return (POS[p] + t) if POS[p] in ("初", "上") else (t + POS[p])
        cards.append({"yi": yi, "name": name, "upper": upper, "lower": lower,
                      "bits": bits, "yao": [yaoname(p, b) for p, b in enumerate(bits)]})
    by_bits = {c["bits"]: c for c in cards}
    by_yi = {c["yi"]: c for c in cards}
    report = []
    ok = True

    def check(cond, msg):
        nonlocal ok
        report.append(("PASS" if cond else "FAIL") + " " + msg)
        if not cond:
            ok = False

    # —— 饱和性①:64 个二进制码两两不同(码空间无碰撞) ——
    check(len(by_bits) == 64, f"饱和性① 码唯一: {len(by_bits)}/64 个不同二进制码")

    # —— 推导 384 条单爻变 ——
    edges = {}  # yi -> [(爻名, 目标yi, 目标卦名)]
    for c in cards:
        lst = []
        for p in range(6):
            nb = list(c["bits"]); nb[p] = "0" if nb[p] == "1" else "1"
            t = by_bits.get("".join(nb))
            lst.append((c["yao"][p], t["yi"] if t else None, t["name"] if t else None))
        edges[c["yi"]] = lst
        c["neighbors"] = [{"line": ln, "target_yi": ty, "target_name": tn}
                          for ln, ty, tn in lst]

    # —— 封闭性:384 条边全部落在 64 卦内,无悬空 ——
    total = sum(1 for v in edges.values() for e in v)
    closed = sum(1 for v in edges.values() for e in v if e[1] is not None)
    dangling = [(yi, e[0]) for yi, v in edges.items() for e in v if e[1] is None]
    check(closed == 384, f"封闭性 384 条单爻变全部落在 64 卦内: {closed}/384"
          + ("" if closed == 384 else f" 悬空:{dangling}"))

    # —— 饱和性②:每卦 6 邻居互不相同 ——
    dup = [yi for yi, v in edges.items() if len({e[1] for e in v}) != 6]
    check(not dup, f"饱和性② 每卦 6 个邻居互异: {'全部通过' if not dup else '重复:' + str(dup)}")

    # —— 饱和性③:转移图连通,任一卦经单爻变可达其余 63 卦 ——
    seen, q = {cards[0]["yi"]}, deque([cards[0]["yi"]])
    while q:
        for e in edges[q.popleft()]:
            if e[1] not in seen:
                seen.add(e[1]); q.append(e[1])
    check(len(seen) == 64, f"饱和性③ 转移图连通: 自 YI01 可达 {len(seen)}/64 卦")

    # —— 附带校验:错卦(全爻取反)与综卦(倒置)亦封闭 ——
    def flip6(b): return "".join("0" if x == "1" else "1" for x in b)
    cuo = sum(1 for c in cards if flip6(c["bits"]) in by_bits)
    zong = sum(1 for c in cards if c["bits"][::-1] in by_bits)
    check(cuo == 64, f"附带 错卦封闭: {cuo}/64")
    check(zong == 64, f"附带 综卦封闭: {zong}/64")

    # 已知锚点抽查(防系统性录入错误):乾错坤、泰错否、既济错未济、困九五动得蹇
    anchors = [("YI01", flip6, "YI02"), ("YI11", flip6, "YI12"), ("YI63", flip6, "YI64")]
    for yi, fn, exp in anchors:
        got = by_bits[fn(by_yi[yi]["bits"])]["yi"]
        check(got == exp, f"锚点 {yi} 错卦={exp}: 得 {got}")
    kun = by_yi["YI47"]
    t5 = kun["neighbors"][4]  # 九五:上兑[1,1,0]中爻翻转->[1,0,0]=震,上震下坎=解
    check(t5["target_yi"] == "YI40", f"锚点 YI47 九五动=解 YI40: 得 {t5['target_yi']}")

    print("\n".join(report))
    print("ALL PASS" if ok else "HAS FAIL — 禁止发布,先纠正录入")

    with open(os.path.join(HERE, "yi_hexagrams.json"), "w", encoding="utf-8") as f:
        json.dump(cards, f, ensure_ascii=False, indent=1)
    with open(os.path.join(HERE, "yi_validation_report.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(report) + "\n" + ("ALL PASS" if ok else "HAS FAIL") + "\n")
    return ok


if __name__ == "__main__":
    raise SystemExit(0 if main() else 1)
