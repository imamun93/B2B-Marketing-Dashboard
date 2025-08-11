import matplotlib.pyplot as plt

# Mock data
campaigns = ["Q3 Podcast Push", "Trade Show 2024", "Email Outreach", "Webinar Series", "Digital Audio Ads"]
mql_sql_conversion = [0.42, 0.35, 0.50, 0.47, 0.40]
revenue = [350000, 250000, 420000, 310000, 275000]
lead_scores = ["High", "Medium", "High", "High", "Medium"]
top_accounts = ["Agency A", "Brand B", "Retailer C", "Startup D", "Brand E"]
account_engagement = [92, 85, 78, 74, 70]

# Create figure
fig, axs = plt.subplots(4, 1, figsize=(10, 16))  # 4 rows, 1 column
fig.suptitle("Unified GTM & B2B Dashboard Concept", fontsize=18, fontweight="bold", y=0.98)

# 1. MQL → SQL Conversion
bars1 = axs[0].bar(campaigns, mql_sql_conversion, color="#4e79a7")
axs[0].set_ylim(0, 0.6)
axs[0].set_ylabel("Conversion Rate")
axs[0].set_title("MQL → SQL Conversion by Campaign", pad=10)
axs[0].set_xticks([])  # Remove x-axis labels
for idx, val in enumerate(mql_sql_conversion):
    axs[0].text(idx, val + 0.01, f"{val*100:.0f}%", ha='center', fontsize=9)
    axs[0].text(idx, -0.05, campaigns[idx], ha='center', fontsize=8, rotation=30)

# 2. Revenue by Campaign
bars2 = axs[1].bar(campaigns, revenue, color="#f28e2b")
axs[1].set_ylabel("Revenue ($)")
axs[1].set_title("Revenue by Campaign", pad=10)
axs[1].set_xticks([])
for idx, val in enumerate(revenue):
    axs[1].text(idx, val + 10000, f"${val:,.0f}", ha='center', fontsize=9)
    axs[1].text(idx, -20000, campaigns[idx], ha='center', fontsize=8, rotation=30)

# 3. Lead Scores
lead_score_colors = {"High": "#59a14f", "Medium": "#edc949", "Low": "#e15759"}
score_map = {"Low": 1, "Medium": 2, "High": 3}
bars3 = axs[2].bar(
    campaigns,
    [score_map[s] for s in lead_scores],
    color=[lead_score_colors[s] for s in lead_scores]
)
axs[2].set_yticks([1, 2, 3])
axs[2].set_yticklabels(["Low", "Medium", "High"])
axs[2].set_title("Lead Scoring Tier", pad=10)
axs[2].set_xticks([])
for idx, val in enumerate(lead_scores):
    axs[2].text(idx, score_map[val] + 0.1, val, ha='center', fontsize=9)
    axs[2].text(idx, 0.5, campaigns[idx], ha='center', fontsize=8, rotation=30)

# 4. Top Engaged Accounts
bars4 = axs[3].bar(top_accounts, account_engagement, color="#af7aa1")
axs[3].set_ylim(0, 100)
axs[3].set_ylabel("Engagement Score")
axs[3].set_title("Top Engaged Accounts This Week", pad=10)
axs[3].set_xticks([])
for idx, val in enumerate(account_engagement):
    axs[3].text(idx, val + 2, f"{val}%", ha='center', fontsize=9)
    axs[3].text(idx, -5, top_accounts[idx], ha='center', fontsize=8, rotation=30)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("sample-visuals.png", bbox_inches="tight")
plt.show()
