# 📏 Biomechanics - Height Measurement of Recumbent Individuals in 2D Space

## 📝 Project Description  
Height is an essential parameter in healthcare, influencing **BMI calculations** and **nutritional planning** for hospitalized patients. While measuring height is straightforward for standing individuals, it becomes **challenging for critically ill and immobile patients**. The absence of an efficient height measurement method for bedridden patients can lead to **gaps in medical care**.  

This project aims to develop a **non-invasive** height measurement system for **recumbent (lying) patients** using **computer vision techniques**.  

To achieve this, we propose two approaches:  
1. **Landmark-Based Method (MediaPipe)**  
   - Extracts **body landmarks** using Google's **MediaPipe** framework.  
   - Uses **geometrical formulas** to calculate skeletal length in **2D space**.  

2. **Bounding Box Method**  
   - Defines a **bounding box** around the patient.  
   - Uses a **pixel-to-height ratio** to estimate the actual height.  
   - Helps improve accuracy when landmark detection fails due to **poor lighting, occlusion, or complex postures**.

📌 **Published Paper:** [Height Measurement of Recumbent Individuals in 2D Space](https://ieeexplore.ieee.org/document/10896362)  
