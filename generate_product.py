#!/usr/bin/env python3
"""
AI量化交易Prompt合集 - PDF生成器
生成精美可售卖的PDF产品
"""
import os
from datetime import datetime

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

def generate_html():
    return """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<style>
@page { margin: 2cm; }
body { font-family: 'Microsoft YaHei', 'PingFang SC', sans-serif; color: #333; line-height: 1.8; max-width: 800px; margin: 0 auto; padding: 20px; }
h1 { color: #1a1a2e; font-size: 28px; text-align: center; border-bottom: 3px solid #e94560; padding-bottom: 15px; margin-bottom: 30px; }
h2 { color: #16213e; font-size: 20px; margin-top: 35px; padding: 8px 15px; background: #f5f5f5; border-left: 4px solid #e94560; }
h3 { color: #0f3460; font-size: 16px; margin-top: 25px; margin-bottom: 5px; }
.prompt-box { background: #f8f9fa; border: 1px solid #dee2e6; border-radius: 8px; padding: 15px 18px; margin: 12px 0; font-family: 'Consolas', 'Courier New', monospace; font-size: 13px; line-height: 1.6; white-space: pre-wrap; word-break: break-word; }
.tag { display: inline-block; background: #e94560; color: white; padding: 2px 10px; border-radius: 12px; font-size: 11px; margin-right: 5px; }
.tag-green { background: #2d6a4f; }
.tag-blue { background: #1a5276; }
.tag-orange { background: #e67e22; }
.cover { text-align: center; padding: 60px 20px; }
.cover h1 { font-size: 36px; border: none; }
.cover .subtitle { font-size: 18px; color: #666; margin: 20px 0; }
.cover .price { font-size: 24px; color: #e94560; font-weight: bold; margin: 30px 0; }
.toc { margin: 30px 0; padding: 20px; background: #fafafa; border-radius: 8px; }
.toc h2 { text-align: center; border: none; background: none; color: #1a1a2e; }
.toc-item { padding: 5px 0; color: #555; }
.section-desc { color: #666; font-size: 14px; margin: -10px 0 20px 0; }
.footer { text-align: center; margin-top: 50px; padding-top: 20px; border-top: 1px solid #ddd; font-size: 12px; color: #999; }
</style>
</head>
<body>

<div class="cover">
<h1>AI量化交易<br>提示词合集</h1>
<div class="subtitle">30个经过验证的专业交易分析Prompt<br>让你用AI做专业级别的市场分析</div>
<div class="price">¥29.9</div>
<p style="color:#888;font-size:14px;">适用于：DeepSeek / GPT-4 / Claude 等主流AI模型</p>
</div>

<div class="toc">
<h2>目录</h2>
<div class="toc-item"><strong>一、技术分析类</strong> — 10个</div>
<div class="toc-item"><strong>二、选股策略类</strong> — 8个</div>
<div class="toc-item"><strong>三、风险控制类</strong> — 5个</div>
<div class="toc-item"><strong>四、AI量化分析类</strong> — 7个</div>
</div>

<!-- ============================================================ -->
<h2>一、技术分析类</h2>
<div class="section-desc">传统技术指标的深度解读，让AI帮你快速识别市场信号</div>

<h3>1. 均线系统分析 <span class="tag">基础</span></h3>
<div class="prompt-box">分析{股票代码}的均线系统：
• 计算MA5/MA10/MA20/MA60的当前位置和斜率方向
• 判断当前处于多头排列还是空头排列
• 识别金叉/死叉信号
• 给出综合买卖评级（强买/弱买/观望/弱卖/强卖）</div>

<h3>2. K线形态识别 <span class="tag">进阶</span></h3>
<div class="prompt-box">识别{股票代码}近30天的K线形态：
• 检测锤子线、吞没形态、十字星、三只乌鸦等经典形态
• 标注每个形态出现的位置和意义
• 结合成交量判断信号强度（强/中/弱）
• 给出操作建议及置信度</div>

<h3>3. MACD背离分析 <span class="tag tag-green">高手</span></h3>
<div class="prompt-box">分析{股票代码}的MACD指标（12,26,9）：
• 识别底背离（股价新低但MACD不新低）
• 识别顶背离（股价新高但MACD不新高）
• 标注背离发生的时间、幅度和持续时间
• 背离后的历史方向概率统计
• 综合操作建议</div>

<h3>4. KDJ超买超卖 <span class="tag">基础</span></h3>
<div class="prompt-box">计算{股票代码}的KDJ指标（9,3,3）：
• 判断K/D/J三线当前数值和位置
• 判断处于超买区（>80）还是超卖区（<20）
• 识别金叉/死叉信号
• 结合趋势线给出反转概率</div>

<h3>5. 布林带压力分析 <span class="tag">进阶</span></h3>
<div class="prompt-box">分析{股票代码}的布林带（20,2）：
• 上轨/中轨/下轨当前数值和通道宽度
• 股价相对于三条轨的位置
• 通道是扩张还是收缩（判断波动率变化）
• 统计近60日价格触及上下轨后的次日方向概率
• 结合开口方向判断突破信号有效性</div>

<h3>6. 量价关系诊断 <span class="tag">进阶</span></h3>
<div class="prompt-box">分析{股票代码}近20个交易日的量价关系：
• 识别放量突破信号（量>均值1.5倍+价涨>3%）
• 识别缩量回调信号（量<均值0.5倍+价跌）
• 识别天量见顶信号（量>均值3倍+上影线）
• 给出整体量价配合评级（优良/中/差）
• 基于量价关系预测短期方向</div>

<h3>7. 支撑阻力位绘制 <span class="tag tag-green">高手</span></h3>
<div class="prompt-box">基于{股票代码}近60日的高低数据：
• 使用聚类算法自动识别关键支撑位（底部密集区）
• 自动识别关键阻力位（顶部密集区）
• 标注每个支撑/阻力位的触碰次数和有效性
• 判断当前价格处于哪个区间
• 给出突破/跌破概率评估</div>

<h3>8. RSI动量分析 <span class="tag">基础</span></h3>
<div class="prompt-box">计算{股票代码}的RSI（14日）：
• 当前RSI数值和趋势方向
• 判断动量强弱（>70超买/30-70中性/<30超卖）
• 识别RSI背离信号
• 结合RSI形态（头肩顶/底）给出趋势反转预警</div>

<h3>9. 多周期共振分析 <span class="tag tag-green">高手</span></h3>
<div class="prompt-box">分析{股票代码}在日线/周线/月线三个周期的信号共振：
• 均线方向是否一致
• MACD方向是否同步
• RSI动量的长中短期一致性
• 若三个周期信号一致，给出强力信号评级
• 若出现分歧，判断哪个周期占主导地位</div>

<h3>10. 量价背离检测 <span class="tag">进阶</span></h3>
<div class="prompt-box">检测{股票代码}近20日的量价背离：
• 价涨量缩（上涨乏力信号）
• 价跌量增（恐慌性抛售）
• 价平量增（主力吸筹信号）
• 统计背离出现后的方向概率
• 结合当前形态给出操作建议</div>

<!-- ============================================================ -->
<h2>二、选股策略类</h2>
<div class="section-desc">高效筛选潜力标的，抓住最佳交易时机</div>

<h3>11. 强势股筛选 <span class="tag tag-blue">策略</span></h3>
<div class="prompt-box">从{板块名称}中筛选强势股：
条件1：近5日涨幅>5%
条件2：今日成交量放大>30%（相比5日均量）
条件3：均线多头排列（MA5>MA10>MA20>MA60）
按综合强度评分排序，给出前5只及每只的入选理由</div>

<h3>12. 放量突破选股 <span class="tag tag-blue">策略</span></h3>
<div class="prompt-box">全市场扫描放量突破信号：
条件1：今日成交量 > 昨日成交量 × 2
条件2：收盘价 > MA20
条件3：今日涨幅 > 3%
按"突破强度 = 量比 × 涨幅"排序
列出前10只个股及技术面评分</div>

<h3>13. 超跌反弹选股 <span class="tag tag-blue">策略</span></h3>
<div class="prompt-box">筛选超跌反弹潜力股：
条件1：近30日跌幅 > 20%
条件2：RSI(14) < 30（超卖）
条件3：今日出现底部放量（量比>1.5）
按"反弹潜力 = 超跌幅度 × 量比"排序
给出前10只及分批建仓建议</div>

<h3>14. 涨停板复盘 <span class="tag tag-blue">策略</span></h3>
<div class="prompt-box">分析今日涨停板数据：
• 统计涨停个股所属板块分布
• 识别龙头股（最先涨停/封单最大/带动板块）
• 识别跟风股（被龙头带动涨停）
• 判断板块热点持续性（跟风股数量多少）
• 给出明日关注方向</div>

<h3>15. 板块轮动分析 <span class="tag tag-orange">宏观</span></h3>
<div class="prompt-box">分析近5日板块轮动：
• 统计各板块资金净流入/流出TOP10
• 判断当前主线板块（连续5日资金流入）
• 判断轮动方向（从哪些板块流出，流向哪些板块）
• 结合政策面和消息面验证轮动逻辑
• 给出下周重点关注板块TOP5</div>

<h3>16. 北向资金跟踪 <span class="tag tag-orange">宏观</span></h3>
<div class="prompt-box">分析北向资金近5日动向：
• 净买入TOP10个股及金额
• 净卖出TOP10个股及金额
• 北向资金整体净流入/流出趋势
• 北向资金主要加仓/减仓行业
• 跟聪明钱的布局方向建议</div>

<h3>17. MACD金叉选股 <span class="tag tag-blue">策略</span></h3>
<div class="prompt-box">全市场扫描今日MACD金叉个股：
条件1：DIF线今日上穿DEA线（刚金叉）
条件2：金叉发生在零轴上方（强势金叉优先）
条件3：成交量放大 > 20%
按金叉强度（DIF与DEA的差距变化）排序
附：该股MACD金叉后历史胜率参考</div>

<h3>18. 均线粘合突破选股 <span class="tag tag-green">高手</span></h3>
<div class="prompt-box">筛选均线粘合后突破的个股：
条件1：MA5/MA10/MA20/MA60四线粘合（最大差距<3%）
条件2：今日放量突破粘合区间上限
条件3：成交量 > 5日均量 × 1.5
• 均线粘合说明主力吸筹完毕，即将拉升
• 给出目标价和止损位
• 历史回测中类似形态的成功概率</div>

<!-- ============================================================ -->
<h2>三、风险控制类</h2>
<div class="section-desc">控制回撤，守住利润，比赚钱更重要</div>

<h3>19. 止损位计算 <span class="tag tag-orange">风控</span></h3>
<div class="prompt-box">为{股票代码}计算合理止损位：
方法1：ATR（14日）止损 = 入场价 - ATR × 2
方法2：支撑位止损 = 最近关键支撑位下方2%
方法3：百分比止损 = 入场价的-5%/-8%/-10%
给出三种风险偏好的方案（保守/稳健/激进）
附：过去20次触及止损后的平均回撤深度</div>

<h3>20. 仓位管理建议 <span class="tag tag-orange">风控</span></h3>
<div class="prompt-box">当前账户：总资产{账户金额}
持仓：{股票代码} {持仓量}股
当前价格：{现价}

分析：
• 该仓位占总资产比例是否合理
• 当前市场波动率水平（高/中/低）
• 建议总仓位控制在{建议比例}以内
• 如需调仓，分批操作的详细计划</div>

<h3>21. 回撤监控预警 <span class="tag tag-orange">风控</span></h3>
<div class="prompt-box">监控{股票代码}从近期高点{最高价}的回撤：
• 当前回撤幅度：{回撤百分比}%
• 回撤速度：快（单日>3%）/ 中 / 慢
• 回撤支撑位分析：下一个支撑在{支撑价}
• 预警：当回撤达到5%/8%/10%分别采取什么行动
• 与同板块其他个股对比，判断是独立下跌还是板块联动</div>

<h3>22. 持仓风险诊断 <span class="tag tag-orange">风控</span></h3>
<div class="prompt-box">诊断当前持仓组合风险：
股票列表：{持股1}/{持股2}/{持股3}（股数/成本/现价）

分析维度：
• 行业集中度：是否过度集中于同一行业
• 仓位集中度：单只个股是否>总资产20%
• 相关性分析：持仓个股之间的相关性系数
• 最大回撤风险：最坏情况下总亏损多少
• 风险对冲建议</div>

<h3>23. 异常波动检测 <span class="tag tag-green">高手</span></h3>
<div class="prompt-box">检测{股票代码}近30日的异常信号：
• 单日跌幅>5%（是否存在利空）
• 成交量>5日均值×3（主力行动信号）
• 日内振幅>8%（多空激烈博弈）
• 连续3日收阴/收阳（趋势确立信号）
• 对每个异常信号给出可能的解释和应对方案</div>

<!-- ============================================================ -->
<h2>四、AI量化分析类</h2>
<div class="section-desc">AI的多维深度分析，超越传统指标的视角</div>

<h3>24. 市场情绪分析 <span class="tag tag-orange">宏观</span></h3>
<div class="prompt-box">对{股票代码}进行市场情绪分析：
步骤1：获取该股最新新闻标题（搜索关键词）
步骤2：对每条新闻进行情感打分（-1到+1）
步骤3：计算综合情绪得分
步骤4：获取雪球/东方财富论坛讨论热度
步骤5：判断目前整体市场情绪（极度悲观/悲观/中性/乐观/极度乐观）
步骤6：情绪面评分及参考价值评估</div>

<h3>25. AI财报解读 <span class="tag tag-orange">宏观</span></h3>
<div class="prompt-box">解读{股票代码}最新财报（{季度年份}）：
核心指标分析：
• 营收：{营收数据} 同比/环比变化
• 净利润：{净利数据} 同比/环比变化
• 毛利率/净利率趋势
• ROE水平和变化
• 资产负债率健康程度
• 现金流质量

综合财务健康评分（1-10分）
与行业平均水平的对比
关注风险点和亮点</div>

<h3>26. 行业对比分析 <span class="tag tag-blue">策略</span></h3>
<div class="prompt-box">将{股票代码}与同行业{同行1}/{同行2}/{同行3}进行对比：

估值对比：
• PE、PB、PS、PCF（当前和历史分位）
• PEG（成长性调整市盈率）

财务对比：
• ROE、ROA、毛利率、净利率
• 营收增长率、利润增长率
• 负债率、流动比率

市场表现对比：
• 年初至今涨幅、近1年涨幅
• 波动率、最大回撤

综合排名及估值是否合理</div>

<h3>27. 事件驱动分析 <span class="tag tag-green">高手</span></h3>
<div class="prompt-box">分析"{事件描述}"对{股票代码}的影响：

影响评估：
• 利好/利空程度（强/中/弱）
• 影响持续时间（短期/中期/长期）
• 影响的确定性（高/中/低）
• 可能的目标涨跌幅空间

历史参考：
• 同类型事件过去对板块的影响幅度
• 市场预期是否已price in

交易策略：
• 激进策略（抢先入场/止损设置）
• 稳健策略（等待确认/分批建仓）
• 对冲策略（如有衍生品）</div>

<h3>28. AI综合买卖决策 <span class="tag tag-green">高手</span></h3>
<div class="prompt-box">对{股票代码}进行多维度综合决策：

技术面评分（权重30%）：
• 均线趋势、MACD、RSI、布林带综合

基本面评分（权重25%）：
• PE/PB分位、ROE、营收增速

资金面评分（权重25%）：
• 主力资金流向、北向资金、成交量变化

情绪面评分（权重20%）：
• 新闻情感分析、社区热度、恐慌/贪婪指数

综合评分及建议：
• 总分（1-100分）及置信区间
• 最终建议：买入/持有/卖出/观望
• 目标价和止损价
• 操作时间窗口</div>

<h3>29. 策略历史回测 <span class="tag tag-green">高手</span></h3>
<div class="prompt-box">对策略"{策略描述}"进行历史回测：

参数设定：
• 回测时间区间：{起始日} 至 {截止日}
• 初始资金：{金额}
• 交易成本：0.1%（佣金+印花税）

回测结果：
• 总收益率（%）
• 年化收益率（%）
• 最大回撤（%）
• 夏普比率
• 胜率（%）
• 盈亏比
• 总交易次数
• 平均持仓天数

结果评估及优化建议</div>

<h3>30. AI每日复盘报告 <span class="tag tag-blue">策略</span></h3>
<div class="prompt-box">生成{股票代码}今日复盘报告：

【今日走势回顾】
• 开盘价/最高价/最低价/收盘价/涨跌幅
• 关键时间节点走势分析
• 分时图量价配合评价

【关键事件解读】
• 今日该股相关新闻/公告
• 板块联动情况
• 大盘影响分析

【技术指标分析】
• 短期/中期/长期趋势判断
• 明日关键支撑/阻力位
• 明日操作计划

【综合评级】
• 明日预期：看涨/震荡/看跌
• 置信度：高/中/低
• 建议操作：买入/持有/减仓/卖出</div>

<!-- ============================================================ -->
<div class="footer">
<p>AI量化交易提示词合集 v1.0</p>
<p>生成日期：""" + datetime.now().strftime("%Y-%m-%d") + """</p>
<p>注意：本产品提供的是AI提示词模板，不构成投资建议。投资有风险，入市需谨慎。</p>
</div>

</body>
</html>"""

def main():
    html = generate_html()
    html_path = os.path.join(OUTPUT_DIR, "AI量化交易Prompt合集.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ HTML 产品文件已生成: {html_path}")
    print(f"   文件大小: {len(html.encode('utf-8')):,} 字节")
    print(f"   HTML可以直接用浏览器打开查看，也可以在线转PDF")

if __name__ == "__main__":
    main()
