# Combinatorics Calculator

![GitHub License](https://img.shields.io/github/license/OldemarCRC/combinatorics-app?style=for-the-badge)
![Python Version](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Framework-Flask-black?style=for-the-badge&logo=flask)

Your go-to web tool for combinatorial calculations and a powerful API for integrating these functions into your own projects! This application helps you easily compute permutations, combinations, and inversions.

---

## 🚀 Features

* **Permutations (P(n,r)):** Calculate the number of ways to arrange 'r' items from a set of 'n' distinct items.
* **Combinations (C(n,r)):** Determine the number of ways to choose 'r' items from a set of 'n' distinct items, without regard to the order of selection.
* **Inversions:** Count the number of inversions in a given permutation sequence.
* **User-Friendly Web Interface:** A clean and intuitive UI to perform calculations.

---

## 🛠️ Technologies Used

* **Backend:** Python 3.11+ with Flask
* **Frontend:** HTML, CSS, JavaScript
* **Web Server:** Gunicorn
* **Containerization:** Docker

---
## 💻 How to Use

### Web Interface

1.  **Select Calculation:** Choose between Permutations, Combinations, or Inversions.
2.  **Enter Values:**
    * For **Permutations** and **Combinations**: Input the "Total number of elements (n)" and "Elements to choose (r)".
    * For **Inversions**: Enter a sequence of numbers separated by spaces (e.g., `3 1 4 2`).
3.  **Calculate:** Click the "Calculate" or "Count Inversions" button.
4.  **View Result:** The result, along with the relevant formula (for P & C), will be displayed. Any errors will be shown in red.
---

## ⚙️ Local Development Setup

To run this project on your local machine:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/OldemarCRC/combinatorics-app.git](https://github.com/OldemarCRC/combinatorics-app.git)
    cd combinatorics-app
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Flask Application:**
    ```bash
    flask run
    # Or for Gunicorn (as in Dockerfile):
    # gunicorn --bind 0.0.0.0:5000 app:app
    ```
    The application will typically run on `http://127.0.0.1:5000/`.

---

## 🐳 Docker Setup

You can also run the application using Docker:

1.  **Build the Docker Image:**
    ```bash
    docker build -t combinatorics-app .
    ```

2.  **Run the Docker Container:**
    ```bash
    docker run -p 5000:5000 combinatorics-app
    ```
    The application will be accessible at `http://localhost:5000/`.

---

## 🤝 Contributing

Feel free to fork the repository, open issues, or submit pull requests. All contributions are welcome!

---

## 📧 Contact

If you have any questions or would like to get in touch, please send an email to:
oldemar.chaves@gmail.com

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

