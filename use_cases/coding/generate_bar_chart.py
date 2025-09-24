# filename: generate_bar_chart.py
import matplotlib.pyplot as plt

# Healthcare applications and the number of papers in each application
healthcare_applications = [
    "Community level work",
    "Risk management/preventive care",
    "Healthcare operation management",
    "Remote care",
    "Early detection",
    "Predictive model building",
    "Calibration",
    "Missing data",
    "Phenotyping",
    "Generative models",
    "Reinforcement learning",
    "Personalized healthcare services",
    "Healthcare Internet of Things (HIoT)",
    "Three-layer architecture for IoT-based healthcare systems",
    "Security threats and solutions",
    "Fairness in classification parity in healthcare",
    "Security and privacy risks of healthcare AI",
    "Cybersecurity research in healthcare AI"
]

# Count of papers in each healthcare application
papers_count = [
    1,  # Community level work
    1,  # Risk management/preventive care
    1,  # Healthcare operation management
    1,  # Remote care
    1,  # Early detection
    1,  # Predictive model building
    1,  # Calibration
    1,  # Missing data
    1,  # Phenotyping
    1,  # Generative models
    1,  # Reinforcement learning
    1,  # Personalized healthcare services
    1,  # Healthcare Internet of Things (HIoT)
    1,  # Three-layer architecture for IoT-based healthcare systems
    1,  # Security threats and solutions
    1,  # Fairness in classification parity in healthcare
    1,  # Security and privacy risks of healthcare AI
    1   # Cybersecurity research in healthcare AI
]

# Create a bar chart
plt.figure(figsize=(12, 6))
plt.barh(healthcare_applications, papers_count, color='skyblue')
plt.xlabel('Number of Papers')
plt.ylabel('Healthcare Applications')
plt.title('Number of Papers in Different Healthcare Applications')
plt.tight_layout()

# Save the bar chart to a file
plt.savefig('healthcare_applications_bar_chart.png')

# Display the bar chart
plt.show()