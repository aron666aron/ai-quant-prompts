#!/usr/bin/env python3
"""
AI量化分析助手 - 命令行工具
基于30个Prompt构建，对接DeepSeek API实现自动化量化分析

用法:
  python quant_analyzer.py stock <代码> [--report brief|full]
  python quant_analyzer.py list-prompts
  python quant_analyzer.py analyze <提示词编号> <股票代码>

示例:
  python quant_analyzer.py stock 000981
  python quant_analyzer.py analyze 1 000981
"""
import os
import sys
import json
import argparse
import urllib.request
import urllib.error

# DeepSeek API 配置
# 建议通过环境变量设置 API_KEY，不要硬编码
API_KEY = os.environ.get("DEEPSEEK_API_KEY", "sk-58b952bfaa2e44c28f7aed91458e41d3")
API_URL = "https://api.deepseek.com/chat/completions"
MODEL = "deepseek-v4-flash"

# ============================================================
# 30个 Prompt 列表（保持与产品一致）
# ============================================================
PROMPTS = {
    1: {
        "name": "均线系统分析",
        "category": "技术分析",
        "prompt": "分析{stock_code}的均线系统：\n• 计算MA5/MA10/MA20/MA60的当前位置和斜率方向\n• 判断当前处于多头排列还是空头排列\n• 识别金叉/死叉信号\n• 给出综合买卖评级（强买/弱买/观望/弱卖/强卖）"
    },
    2: {
        "name": "K线形态识别",
        "category": "技术分析",
        "prompt": "识别{stock_code}近30天的K线形态：\n• 检测锤子线、吞没形态、十字星、三只乌鸦等经典形态\n• 结合成交量判断信号强度\n• 给出操作建议及置信度"
    },
    3: {
        "name": "MACD背离分析",
        "category": "技术分析",
        "prompt": "分析{stock_code}的MACD指标（12,26,9）：\n• 识别底背离和顶背离\n• 标注背离发生的时间、幅度和持续时间\n• 背离后的历史方向概率统计"
    },
    4: {
        "name": "KDJ超买超卖",
        "category": "技术分析",
        "prompt": "计算{stock_code}的KDJ指标（9,3,3）：\n• K/D/J三线当前数值\n• 是否处于超买区（>80）或超卖区（<20）\n• 识别金叉/死叉信号"
    },
    5: {
        "name": "布林带压力分析",
        "category": "技术分析",
        "prompt": "分析{stock_code}的布林带（20,2）：\n• 上轨/中轨/下轨位置和通道宽度\n• 通道扩张还是收缩\n• 近60日价格触及上下轨后的次日方向概率"
    },
    6: {
        "name": "量价关系诊断",
        "category": "技术分析",
        "prompt": "分析{stock_code}近20个交易日的量价关系：\n• 识别放量突破、缩量回调、天量见顶信号\n• 综合量价配合评级\n• 基于量价关系预测短期方向"
    },
    7: {
        "name": "支撑阻力位绘制",
        "category": "技术分析",
        "prompt": "基于{stock_code}近60日的高低数据：\n• 自动识别关键支撑位和阻力位\n• 标注每个支撑/阻力位的有效性\n• 给出突破/跌破概率评估"
    },
    8: {
        "name": "RSI动量分析",
        "category": "技术分析",
        "prompt": "计算{stock_code}的RSI（14日）：\n• 当前RSI数值和趋势方向\n• 判断动量方向\n• 识别RSI背离信号"
    },
    17: {
        "name": "MACD金叉选股",
        "category": "选股策略",
        "prompt": "全市场扫描今日MACD金叉个股：\n条件1：DIF线上穿DEA线（刚金叉）\n条件2：金叉发生在零轴上方\n条件3：成交量放大>20%\n按金叉强度排序，附历史胜率参考"
    },
    28: {
        "name": "AI综合买卖决策",
        "category": "AI量化分析",
        "prompt": "对{stock_code}进行多维度综合决策：\n\n1. 技术面评分（权重30%）：均线趋势、MACD、RSI、布林带\n2. 基本面评分（权重25%）：PE/PB分位、ROE、营收增速\n3. 资金面评分（权重25%）：主力资金、成交量\n4. 情绪面评分（权重20%）：新闻情感、市场热度\n\n给出综合评分（1-100分）及买入/持有/卖出建议"
    },
    30: {
        "name": "AI每日复盘报告",
        "category": "AI量化分析",
        "prompt": "生成{stock_code}今日复盘报告：\n\n【今日走势回顾】\n开盘价/最高价/最低价/收盘价/涨跌幅\n关键时间节点走势分析\n\n【技术指标分析】\n短期/中期/长期趋势判断\n明日关键支撑/阻力位\n明日操作计划\n\n【综合评级】\n明日预期及置信度"
    }
}


def call_deepseek(prompt_text):
    """调用 DeepSeek API"""
    messages = [
        {"role": "system", "content": "你是一位专业的量化交易分析师，精通A股技术分析和基本面分析。请基于你掌握的金融知识进行分析，输出专业、简洁的分析报告。注意：你无法获取实时数据，请根据用户的输入数据和你的金融知识进行推演分析。"},
        {"role": "user", "content": prompt_text}
    ]
    
    payload = {
        "model": MODEL,
        "messages": messages,
        "stream": False,
        "max_tokens": 4096
    }
    
    req = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        method="POST"
    )
    
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            return result["choices"][0]["message"]["content"]
    except urllib.error.HTTPError as e:
        return f"[API错误] HTTP {e.code}: {e.read().decode('utf-8')}"
    except urllib.error.URLError as e:
        return f"[网络错误] 无法连接到API: {e.reason}"
    except Exception as e:
        return f"[错误] {str(e)}"


def list_prompts():
    """列出所有可用Prompt"""
    print("\n" + "=" * 60)
    print("  📊 AI量化分析助手 - 可用分析工具")
    print("=" * 60)
    
    categories = {}
    for num, info in sorted(PROMPTS.items()):
        cat = info["category"]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append((num, info["name"]))
    
    for cat, items in categories.items():
        print(f"\n  【{cat}】")
        for num, name in items:
            print(f"    {num:2d}. {name}")
    
    print("\n" + "=" * 60)
    print("  使用: python quant_analyzer.py analyze <编号> <股票代码>")
    print("  示例: python quant_analyzer.py analyze 1 000981")
    print("=" * 60 + "\n")


def analyze(prompt_num, stock_code):
    """使用指定Prompt分析股票"""
    if prompt_num not in PROMPTS:
        print(f"❌ 错误: 提示词 #{prompt_num} 不存在")
        print(f"   支持: {sorted(PROMPTS.keys())}")
        return
    
    info = PROMPTS[prompt_num]
    prompt_text = info["prompt"].format(stock_code=stock_code)
    
    print(f"\n{'=' * 60}")
    print(f"  📈 {info['name']} — {stock_code}")
    print(f"  🏷  {info['category']}")
    print(f"{'=' * 60}\n")
    print(f"  ⏳ 正在调用 DeepSeek V4 Flash 分析中...\n")
    
    result = call_deepseek(prompt_text)
    
    print(f"{'=' * 60}")
    print(f"  📋 分析结果")
    print(f"{'=' * 60}\n")
    print(result)
    print(f"\n{'=' * 60}")
    print(f"  分析完成 | 模型: {MODEL}")
    print(f"{'=' * 60}\n")


def quick_report(stock_code, mode="brief"):
    """快速综合报告"""
    print(f"\n{'=' * 60}")
    print(f"  📊 {stock_code} 综合量化分析")
    print(f"{'=' * 60}\n")
    
    if mode == "brief":
        prompt_text = PROMPTS[28]["prompt"].format(stock_code=stock_code)
    else:
        prompt_text = f"""请为股票 {stock_code} 生成一份完整的量化分析报告：
        
1. 【公司概况】主营业务、行业地位、市值规模
2. 【技术分析】均线趋势、MACD、RSI、布林带综合分析
3. 【估值分析】PE/PB分位、行业对比
4. 【资金面】近期成交量变化、主力资金动向
5. 【风险提示】当前主要风险
6. 【综合建议】买入/持有/卖出及理由
7. 【关键价位】支撑位、阻力位、目标价"""
    
    print(f"  ⏳ 正在生成完整报告...\n")
    result = call_deepseek(prompt_text)
    print(result)
    print(f"\n{'=' * 60}")
    print(f"  报告完成")
    print(f"{'=' * 60}\n")


def main():
    parser = argparse.ArgumentParser(
        description="AI量化分析助手 - 基于DeepSeek的量化交易分析工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="示例:\n  %(prog)s stock 000981          # 快速分析\n  %(prog)s analyze 1 000981     # 指定Prompt分析\n  %(prog)s list-prompts          # 列出所有可用的Prompt"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="可用命令")
    
    # stock 快速分析
    stock_parser = subparsers.add_parser("stock", help="快速分析股票")
    stock_parser.add_argument("code", help="股票代码，如 000981")
    stock_parser.add_argument("--report", choices=["brief", "full"], default="brief", help="报告模式")
    
    # analyze 指定Prompt分析
    analyze_parser = subparsers.add_parser("analyze", help="使用指定Prompt分析")
    analyze_parser.add_argument("num", type=int, help="Prompt编号（使用list-prompts查看）")
    analyze_parser.add_argument("code", help="股票代码")
    
    # list-prompts 列出所有Prompt
    subparsers.add_parser("list-prompts", help="列出所有可用的分析工具")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        print("\n  快速开始:")
        print("    python quant_analyzer.py list-prompts")
        print("    python quant_analyzer.py stock 000981")
        print("    python quant_analyzer.py analyze 1 000981")
        return
    
    if args.command == "list-prompts":
        list_prompts()
    elif args.command == "analyze":
        analyze(args.num, args.code)
    elif args.command == "stock":
        quick_report(args.code, args.report)


if __name__ == "__main__":
    main()
