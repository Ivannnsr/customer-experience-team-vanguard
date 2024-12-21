# Vanguard A/B Test Analysis

## Introduction
Welcome to the Vanguard A/B Test Analysis project! This project is part of Module 2, Unit 11 - Statistics. In this project, we apply various data analysis techniques to evaluate the effectiveness of a new User Interface (UI) design for Vanguard's online process. The goal is to determine if the new design leads to a better user experience and higher process completion rates.

## Project Overview
You are a newly employed data analyst in the Customer Experience (CX) team at Vanguard. Your task is to analyze the results of a digital experiment comparing a traditional online process (Control Group) with a new, modern UI (Test Group). The experiment was conducted from 3/15/2017 to 6/20/2017.

## Data Overview
We used three datasets for this analysis:
1. **Client Profiles (df_final_demo)**: Demographics like age, gender, and account details of our clients.
2. **Digital Footprints (df_final_web_data)**: A detailed trace of client interactions online, divided into two parts: pt_1 and pt_2.
3. **Experiment Roster (df_final_experiment_clients)**: A list revealing which clients were part of the grand experiment.

## Data Cleaning and Merging
We performed the following steps to clean and merge the datasets:
- Converted column names to lowercase.
- Merged the client profiles with the experiment roster.
- Concatenated the two parts of the digital footprints dataset.
- Merged the combined client profiles with the digital footprints.

## Data Analysis
### Pivot Table
We created a pivot table to summarize the client interactions at each process step and added visit counts and variation columns.

### Time Analysis
We calculated the time spent by users in each step of the process.

### Error Analysis
We identified users with time_in_step between 0 and 2 seconds and calculated backward steps per visit and per user.

### Demographic Analysis
We analyzed the mean and median age and tenure of clients, as well as the gender distribution.

## Performance Metrics
We defined the following KPIs to evaluate the new design's performance:
- **Completion Rate**: The proportion of users who reach the final ‘confirm’ step.
- **Time Spent on Each Step**: The average duration users spend on each step.
- **Error Rates**: The rate at which users move from a later step to an earlier one.

## Hypothesis Testing
### Completion Rate Comparison
We performed a one-sided two-proportion z-test to compare the completion rates between the Test and Control groups.

### Completion Rate with Cost-Effectiveness Threshold
We checked if the observed increase in completion rate meets or exceeds the 5% threshold set by Vanguard.

### Additional Hypotheses
We tested additional hypotheses related to average age, client tenure, and gender distribution between the Test and Control groups.

## Experiment Evaluation
We evaluated the experiment design, duration, and additional data needs:
- **Design Effectiveness**: The experiment was well-structured, with clients randomly and equally divided between the old and new designs.
- **Duration Assessment**: The timeframe of the experiment was adequate to gather meaningful data and insights.
- **Additional Data Needs**: User feedback on the new design, detailed interaction logs, and data on user satisfaction and engagement could enhance the analysis.

## Additional Analysis
### Day of the Week Analysis
We analyzed the distribution of 'confirm' steps across different days of the week.

## Streamlit App
We have also developed a Streamlit app to provide an interactive way to explore the results of our analysis.

## Conclusion
The analysis provides valuable insights into the effectiveness of the new UI design. The new design leads to a higher completion rate, and the observed increase is statistically significant. However, the increase does not meet the 5% threshold set for cost-effectiveness. Further improvements and targeted strategies are recommended to enhance the design's effectiveness.

## Team Members
- [Cris](https://github.com/cdeniaca)
- [Javi](https://github.com/JavierRodriguezdeCea)
- [Ivan](https://github.com/Ivannnsr)
- [Miqueas](https://github.com/miqueasmd)


