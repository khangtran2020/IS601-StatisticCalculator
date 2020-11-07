# Margin of Error
The margin of error is a statistic expressing the amount of random sampling error in the results of a survey. The larger the margin of error, the less confidence one should have that a poll result would reflect the result of a survey of the entire population. The margin of error will be positive whenever a population is incompletely sampled and the outcome measure has positive variance, which is to say, the measure varies.

The term margin of error is often used in non-survey contexts to indicate observational error in reporting measured quantities.

Margin of Error: The amount allowed for miscalculation.

    margin_of_error = z_critical * (stdev/math.sqrt(sample_size))
Z-critical: The number of standard deviations you'd have to go from the mean of the normal distribution to capture the proportion of the data associated with the desired confidence level. If four cover that range, the Z-critical would be 2.

    z_critical = stats.norm.ppf(q = 0.975) #q = confidence interval of 95%
    
https://en.wikipedia.org/wiki/Margin_of_error
