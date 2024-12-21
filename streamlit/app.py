
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.proportion import proportions_ztest
from scipy.stats import ttest_ind, chi2_contingency

# URLs for the datasets
df_final_demo_url = r'https://raw.githubusercontent.com/data-bootcamp-v4/lessons/refs/heads/main/5_6_eda_inf_stats_tableau/project/files_for_project/df_final_demo.txt'
df_final_web_data_pt1_url = r'https://raw.githubusercontent.com/data-bootcamp-v4/lessons/refs/heads/main/5_6_eda_inf_stats_tableau/project/files_for_project/df_final_web_data_pt_1.txt'
df_final_web_data_pt2_url = r'https://raw.githubusercontent.com/data-bootcamp-v4/lessons/refs/heads/main/5_6_eda_inf_stats_tableau/project/files_for_project/df_final_web_data_pt_2.txt'
df_final_experiment_client_url = r'https://raw.githubusercontent.com/data-bootcamp-v4/lessons/refs/heads/main/5_6_eda_inf_stats_tableau/project/files_for_project/df_final_experiment_clients.txt'

# Load the datasets
try:
    df_final_demo = pd.read_csv(df_final_demo_url, sep=',')
    df_final_web_data_pt1 = pd.read_csv(df_final_web_data_pt1_url, sep=',')
    df_final_web_data_pt2 = pd.read_csv(df_final_web_data_pt2_url, sep=',')
    df_final_experiment_client = pd.read_csv(df_final_experiment_client_url, sep=',')
except Exception as e:
    print(f"Error loading the file: {e}")
    
# Merge the datasets
final_demo = pd.merge(df_final_demo, df_final_experiment_client, on='client_id')
final_demo = final_demo.dropna()

# Concatenate web data parts
final_web = pd.concat([df_final_web_data_pt1, df_final_web_data_pt2], ignore_index=True)

# Merge final_demo with final_web
tabla_analisis = pd.merge(final_demo, final_web, on='client_id')

def calculate_completion_rates():
    test_completions = 25716
    control_completions = 17498
    test_total = 177787
    control_total = 143408

    completion_rate_test = test_completions / test_total
    completion_rate_control = control_completions / control_total
    observed_increase = completion_rate_test - completion_rate_control

    return completion_rate_test, completion_rate_control, observed_increase

def plot_completion_rates(completion_rate_test, completion_rate_control):
    rates = pd.DataFrame({
        'Group': ['Test', 'Control'],
        'Completion Rate': [completion_rate_test, completion_rate_control]
    })
    fig, ax = plt.subplots()
    sns.barplot(x='Group', y='Completion Rate', data=rates, ax=ax)
    return fig

def hypothesis_testing():
    test_completions = 25716
    control_completions = 17498
    test_total = 177787
    control_total = 143408

    count = [test_completions, control_completions]
    nobs = [test_total, control_total]
    stat, p_value = proportions_ztest(count, nobs, alternative='larger')

    return stat, p_value

st.title('Vanguard A/B Test Analysis')

st.header('Completion Rates')
completion_rate_test, completion_rate_control, observed_increase = calculate_completion_rates()
st.write(f"Completion Rate (Test): {completion_rate_test:.4f}")
st.write(f"Completion Rate (Control): {completion_rate_control:.4f}")
st.write(f"Observed Increase: {observed_increase:.4f}")

fig = plot_completion_rates(completion_rate_test, completion_rate_control)
st.pyplot(fig)

st.header('Hypothesis Testing')
stat, p_value = hypothesis_testing()
st.write(f"Test Statistic: {stat}")
st.write(f"P-value: {p_value}")

if p_value < 0.05:
    st.write("Reject the null hypothesis: The observed increase in completion rate is statistically significant.")
else:
    st.write("Fail to reject the null hypothesis: The observed increase in completion rate is not statistically significant.")