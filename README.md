# Vanguard A/B Test Analysis  

## Introduction  
Welcome to the Vanguard A/B Test Analysis project! This project is part of Module 2, Unit 11 - Statistics. In this project, we apply various data analysis techniques to evaluate the effectiveness of a new User Interface (UI) design for Vanguard's online process. The goal is to determine if the new design leads to a better user experience and higher process completion rates.  

## Project Overview  
As a data analyst in the Customer Experience (CX) team at Vanguard, your role is to analyze the results of a digital experiment comparing a traditional online process (Control Group) with a new, modern UI (Test Group). The experiment was conducted from 3/15/2017 to 6/20/2017.  

The data for this analysis was collected using digital measurement tools that recorded **event-based interactions** with the new User Interface. These events include actions users took while navigating through the process, providing insights into their behavior and engagement with the design.  

## Data Overview  
We used three datasets for this analysis:  
1. **Client Profiles (df_final_demo):** Demographics like age, gender, and account details of our clients.  
2. **Digital Footprints (df_final_web_data):** A detailed trace of client interactions online, divided into two parts: pt_1 and pt_2. These records represent **event-based data** tracking user interactions with the UI.  
3. **Experiment Roster (df_final_experiment_clients):** A list revealing which clients were part of the grand experiment.  

## Data Cleaning and Merging  
The following steps were performed to prepare the data for analysis:  
- Converted column names to lowercase for consistency.  
- Merged the client profiles with the experiment roster to identify participants and their group assignments.  
- Concatenated the two parts of the digital footprints dataset for a complete interaction dataset.  
- Merged the combined client profiles with the digital footprints for a holistic view.  

## Data Analysis  
### Pivot Table  
A pivot table was created to summarize client interactions at each process step, including visit counts and variation columns.  

### Time Analysis  
The time spent by users at each step of the process was calculated to understand engagement levels.  

### Error Analysis  
Users with time_in_step between 0 and 2 seconds were flagged, and backward steps were calculated per visit and per user to identify navigation issues.  

### Demographic Analysis  
We analyzed demographic data, including the mean and median age, client tenure, and gender distribution.  

## Performance Metrics  
To evaluate the new design's performance, we defined the following KPIs:  
- **Completion Rate:** The proportion of users reaching the final ‘confirm’ step.  
- **Time Spent on Each Step:** The average duration users spend on each step of the process.  
- **Error Rates:** The frequency at which users moved backward from a later step to an earlier one.  

## Hypothesis Testing  
### Completion Rate Comparison  
A one-sided two-proportion z-test was performed to compare completion rates between the Test and Control groups.  

### Completion Rate with Cost-Effectiveness Threshold  
We verified if the observed increase in completion rate met or exceeded the 5% threshold set by Vanguard for cost-effectiveness.  

### Additional Hypotheses  
Additional hypotheses were tested regarding average age, client tenure, and gender distribution across Test and Control groups.  

## Experiment Evaluation  
- **Design Effectiveness:** The experiment was well-structured, with clients randomly and equally divided between the old and new designs.  
- **Duration Assessment:** The timeframe of the experiment (3 months) was sufficient for meaningful analysis.  
- **Additional Data Needs:** User feedback, detailed interaction logs, and data on satisfaction and engagement could further enrich the analysis.  

## Additional Analysis  
### Day of the Week Analysis  
We analyzed the distribution of 'confirm' steps across different days to identify potential temporal patterns.  

## Streamlit App  
An interactive **Streamlit app** was developed to explore the analysis results dynamically, enabling users to visualize the data and insights effectively.  

## Conclusion  
The analysis revealed that the new UI design led to a higher completion rate, with a statistically significant improvement over the traditional design. However, the increase did not meet the 5% threshold required for cost-effectiveness.  
This suggests that while the new design shows promise, further enhancements and targeted strategies are needed to maximize its impact on user experience and process completion rates.  


## Team Members
- [Cris](https://github.com/cdeniaca)
- [Javi](https://github.com/JavierRodriguezdeCea)
- [Ivan](https://github.com/Ivannnsr)
- [Miqueas](https://github.com/miqueasmd)


