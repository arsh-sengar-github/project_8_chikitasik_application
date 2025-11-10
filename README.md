<a id="top"></a>

[![Issues][issues-shield]][issues-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Contributors][contributors-shield]][contributors-url]

<br />

<!-- LOGO -->

<div align="center">

  <a href="https://project-8-chikitasik-application-shqg5c8nfney7vbpajcyh8.streamlit.app/">
    <img src="public/chikitasik_logo.png" alt="Logo" width="100" height="100">
  </a>

  <h3 align="center">Chikitasik</h3>

  <p align="center">
    Chikitasik is a Streamlit-based machine learning web application that predicts the likelihood of heart disease using a trained Random Forest model. Built for accessibility and clarity, it helps users make informed health predictions through an interactive and intuitive interface.
    <br />
    <a href="https://github.com/arsh-sengar-github/project_8_chikitasik_application">
    <strong>Explore Documents »</strong>
    </a>
    <br />
    <br />
    <a href="https://project-8-chikitasik-application-shqg5c8nfney7vbpajcyh8.streamlit.app/">View Demonstration</a>
    &middot;
    <a href="https://github.com/arsh-sengar-github/project_8_chikitasik_application/issues/new?labels=bug&template=bug-report---.md">Report a Bug</a>
    &middot;
    <a href="https://github.com/arsh-sengar-github/project_8_chikitasik_application/issues/new?labels=enhancement&template=feature-request---.md">Request a Feature</a>
  </p>

</div>

<!-- CONTENTS -->

<details>

  <summary>Contents</summary>

  <ol>
  
  <li>
  <a href="#acknowledgment">Acknowledgment</a>
  </li>
    <li>
      <a href="#about">About</a>
      <ul>
        <li>
        <a href="#technologies">Technologies</a>
        </li>
      </ul>
    </li>
    <li>
      <a href="#start">Start</a>
      <ul>
        <li>
        <a href="#prerequisites">Prerequisites</a>
        </li>
        <li>
        <a href="#installation">Installation</a>
        </li>
      </ul>
    </li>
    <li>
    <a href="#usage">Usage</a>
    </li>
    <li>
    <a href="#contribution">Contribution</a>
    </li>
    <li>
    <a href="#contact">Contact</a>
    </li>

  </ol>

</details>

<!-- ACKNOWLEDGMENT -->

## Acknowledgment

Special thanks to the open-source tools, datasets, and communities that made **Chikitasik** possible:

- [Streamlit](https://streamlit.io/)
- [scikit-learn](https://scikit-learn.org/)
- [pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Kaggle Datasets](https://www.kaggle.com/)
- The global data science community for inspiring open collaboration and learning.

---

<p align="right">
(<a href="#top">back to top</a>)
</p>

---

<!-- ABOUT -->

## About

[![Screen Shot][screenshot]](https://project-8-chikitasik-application-shqg5c8nfney7vbpajcyh8.streamlit.app/)

---

## 🩺 About Chikitasik

**Chikitasik** is a machine learning–powered web application that predicts whether an individual is at risk of **heart disease**.  
The model was trained on real-world health data and integrated into a **Streamlit UI** for real-time, user-friendly predictions.

The name **“Chikitasik”** (from _chikitsa_, meaning “treatment” or “care” in Sanskrit) reflects its goal — to assist in early risk detection and awareness through intelligent technology.

### 🌐 Universal Pages

- **Landing:**  
  The main interface welcomes users to **Chikitasik**, providing an intuitive form to input essential medical parameters such as:

  - Age, Sex, and Chest Pain Type
  - Resting Blood Pressure and Cholesterol
  - Fasting Blood Sugar and Maximum Heart Rate
  - Exercise-Induced Angina, ST Depression, and Slope

  Once all parameters are filled, users click **“Predict Heart Risk”** to run the trained machine learning model and obtain real-time insights.

  Displays a clear **diagnostic result**, showing whether the individual is **high or low risk of heart disease**.

  Results update instantly for every new input, enabling users to experiment with different health conditions and observe changing outcomes.

---

<p align="right">
(<a href="#top">back to top</a>)
</p>

---

### ⚙️ Technologies

**Chikitasik** is built on a reliable data science and web framework stack, ensuring accurate predictions, smooth interaction, and a clean interface for real-time health risk assessment.

- [![Python][Python]][Python-url]
- [![Streamlit][Streamlit]][Streamlit-url]
- [![Pandas][Pandas]][Pandas-url]
- [![NumPy][NumPy]][NumPy-url]
- [![Scikit-learn][Scikit-learn]][Scikit-learn-url]

---

| Category                   | Stack / Tools                                          |
| -------------------------- | ------------------------------------------------------ |
| **Framework & Interface**  | Streamlit                                              |
| **Language & Core**        | Python                                                 |
| **Data Handling**          | Pandas, NumPy                                          |
| **Machine Learning**       | Scikit-learn, Pickle                                   |
| **Model & Data Files**     | `heart_disease_rf_model.pkl`, `heart_disease_data.csv` |
| **Development & Workflow** | Virtual Environment, Git, GitHub                       |

---

<p align="right">
(<a href="#top">back to top</a>)
</p>

---

<!-- START -->

## Start

Follow these steps to run **Chikitasik** locally for development and testing.

---

<p align="right">
(<a href="#top">back to top</a>)
</p>

---

### 📋 Prerequisites

Ensure you have the following installed:

- **Python 3.12+**
- **pip**
- **virtualenv** _(optional but recommended)_

---

### 📥 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/arsh-sengar-github/project_8_chikitasik_application.git
   ```

2. **Navigate into the project directory**

   ```bash
   cd project_8_chikitasik_application
   ```

3. **(Optional) Create and activate a virtual environment**

   ```bash
   python -m venv project_8_virtual_environment
   source project_8_virtual_environment/Scripts/activate  # On Windows
   ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the development server**

   ```bash
   streamlit run app.py
   ```

6. **Open the app**
   Visit [http://localhost:8501](http://localhost:8501) to view **Chikitasik** in your browser.

---

<p align="right">
(<a href="#top">back to top</a>)
</p>

---

<!-- USAGE -->

## Usage

The app provides an intuitive interface for real-time predictions.

Enter patient information such as:

- **Age**
- **Sex**
- **Chest pain type**
- **Resting blood pressure**
- **Cholesterol**
- **Fasting blood sugar**
- **Maximum heart rate achieved**
- **Exercise-induced angina**
- **ST depression**, **slope**, etc.

Click **Predict** to view:

- A prediction label:  
  **“high risk of heart disease”** or **“low risk of heart disease.”**
- A confidence score derived from the trained **Random Forest** model.

Optionally, explore the dataset insights and visualizations in the accompanying notebook:

📘 `project_8_notebook/heart_disease_predictor.ipynb`

---

<p align="right">
(<a href="#top">back to top</a>)
</p>

---

<!-- CONTRIBUTION -->

## Contribution

Contributions are what make the open-source community such an inspiring space to **learn**, **collaborate**, and **create**.
Any contributions you make to **Chikitasik** are **deeply appreciated** — whether it’s improving the UI, optimizing backend logic, or suggesting new features!

If you have an idea to make this project even better, feel free to **fork** the repository and submit a **pull request**.
Alternatively, you can simply open an **issue** with the label `enhancement`.

And of course — don’t forget to ⭐ **star the repo** if you like what you see!

---

### ❓ How to Contribute

1. **Fork** the Project
2. **Create your Feature Branch**

   ```bash
   git checkout -b feature/AmazingFeature
   ```

3. **Commit your Changes**

   ```bash
   git commit -m 'Add some AmazingFeature'
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/AmazingFeature
   ```

5. **Open a Pull Request**

---

### 👨‍💻 Top Contributors

<a href="https://github.com/arsh-sengar-github/project_8_chikitasik_application/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=arsh-sengar-github/project_8_chikitasik_application" alt="Contributors Graph" />
</a>

---

<p align="right">
(<a href="#top">back to top</a>)
</p>

---

<!-- CONTACT -->

## Contact

**Project Maintainer:** [Arsh Sengar](https://github.com/arsh-sengar-github)

📧 **Email:** [arshsengar.academic@gmail.com](mailto:arshsengar.academic@gmail.com)

📁 **Repository:** [https://github.com/arsh-sengar-github/project_8_chikitasik_application](https://github.com/arsh-sengar-github/project_8_chikitasik_application)

🌐 **Application:** [https://project-8-chikitasik-application-shqg5c8nfney7vbpajcyh8.streamlit.app](https://project-8-chikitasik-application-shqg5c8nfney7vbpajcyh8.streamlit.app)

If you have any questions, feedback, or suggestions, feel free to reach out!
Collaboration and constructive ideas are always welcome. 💡

---

<p align="right">
(<a href="#top">back to top</a>)
</p>

---

<!-- Badge Definitions -->

[issues-shield]: https://img.shields.io/github/issues/arsh-sengar-github/project_8_chikitasik_application.svg?style=for-the-badge
[issues-url]: https://github.com/arsh-sengar-github/project_8_chikitasik_application/issues
[forks-shield]: https://img.shields.io/github/forks/arsh-sengar-github/project_8_chikitasik_application.svg?style=for-the-badge
[forks-url]: https://github.com/arsh-sengar-github/project_8_chikitasik_application/network/members
[stars-shield]: https://img.shields.io/github/stars/arsh-sengar-github/project_8_chikitasik_application.svg?style=for-the-badge
[stars-url]: https://github.com/arsh-sengar-github/project_8_chikitasik_application/stargazers
[contributors-shield]: https://img.shields.io/github/contributors/arsh-sengar-github/project_8_chikitasik_application.svg?style=for-the-badge
[contributors-url]: https://github.com/arsh-sengar-github/project_8_chikitasik_application/graphs/contributors
[screenshot]: public/chikitasik.png
[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Streamlit]: https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white
[Streamlit-url]: https://streamlit.io/
[Pandas]: https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white
[Pandas-url]: https://pandas.pydata.org/
[NumPy]: https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white
[NumPy-url]: https://numpy.org/
[Scikit-learn]: https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white
[Scikit-learn-url]: https://scikit-learn.org/
