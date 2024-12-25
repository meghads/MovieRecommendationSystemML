# Movie Recommendation System

This project implements a **content-based** and **popular-based recommendation system** using Python and machine learning. The system suggests movies based on user preferences by analyzing features such as genres, keywords, tagline, cast, and director.

---

## Features

- **Content-Based Filtering**: Suggests movies similar to the user's input based on textual feature analysis.
- **Popular-Based Recommendations**: Highlights movies that are highly similar based on combined features.
- **Machine Learning Techniques**: Uses TF-IDF Vectorization and Cosine Similarity for feature extraction and similarity calculations.

---

## How It Works

1. **Data Collection**:
   - The system loads movie data from a CSV file (`movies.csv`), which contains information like title, genres, keywords, tagline, cast, and director.

2. **Data Preprocessing**:
   - Missing values in the relevant features are replaced with empty strings.
   - Selected features are combined into a single string for each movie to create a unified data representation.

3. **Feature Extraction**:
   - Textual data is transformed into numerical vectors using **TF-IDF Vectorization** to quantify textual relevance.

4. **Similarity Calculation**:
   - Movie similarity is calculated using **Cosine Similarity**, which measures the angular distance between the feature vectors.

5. **Movie Recommendation**:
   - The user inputs their favorite movie name.
   - The system identifies the closest match for the provided movie name.
   - It then sorts and displays the top 15 most similar movies based on the calculated similarity scores.

---

## Steps to Run the System

1. **Clone the Repository**: 
   Download or clone the repository to your local machine.

2. **Prepare the Dataset**:
   Ensure you have a CSV file named `movies.csv` in the same directory as the script. The CSV should include:
   - `title` (Movie titles)
   - `genres`
   - `keywords`
   - `tagline`
   - `cast`
   - `director`

3. **Run the Script**:
   - Navigate to the project directory in your terminal or IDE.
   - Execute the script with the command:
     ```bash
     python MovieRecommendation.py
     ```

4. **Enter Your Favorite Movie**:
   - When prompted, type the name of your favorite movie.
   - The system will output a list of 15 movies similar to the one you entered.

---

## Example Interaction

```plaintext
Enter your favourite movie name: Inception
Movies suggested for you:

1. Interstellar
2. The Dark Knight
3. The Prestige
4. Memento
5. Tenet
6. Shutter Island
7. The Matrix
8. Avatar
9. The Social Network
10. Fight Club
...
