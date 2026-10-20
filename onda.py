# import pandas as pd
# import json

# # 1. 各GAIからのJSON抽出データの読み込み（例）
# gpt_data = [{"Company": "SpaceX", "Item": "IJV Ultrasound", "Status": "Mandatory"}]
# claude_data = [{"Company": "SpaceX", "Item": "IJV Ultrasound", "Status": "Mandatory"}]
# gemini_data = [{"Company": "SpaceX", "Item": "IJV Ultrasound", "Status": "Recommended"}]

# df_gpt = pd.DataFrame(gpt_data).assign(GAI="GPT-4o")
# df_claude = pd.DataFrame(claude_data).assign(GAI="Claude3.5")
# df_gemini = pd.DataFrame(gemini_data).assign(GAI="Gemini1.5")

# # 2. データのマージとピボットテーブル作成
# merged = pd.concat([df_gpt, df_claude, df_gemini])
# pivot = pd.pivot_table(merged, index=['Company', 'Item'], columns='GAI', values='Status', aggfunc='first')

# # 3. Consensus（一致度）の自動解析関数
# def evaluate_consensus(row):
#     vals = [str(x).strip() for x in row.dropna()]
#     unique_vals = set(vals)
#     if len(unique_vals) == 1:
#         return "Full Agreement"
#     elif len(vals) == 3 and len(unique_vals) == 2:
#         return "Majority Vote (Review Required)"
#     else:
#         return "Conflict (Human Adjudication Needed)"

# pivot['Consensus_Status'] = pivot.apply(evaluate_consensus, axis=1)
# print(pivot)

for i in range(1, 4):
    print(" " * (3 - i))
    print("*" * ((i * 2) - 1))