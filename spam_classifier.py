import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def main():
    # Load the dataset
    df = pd.read_csv('spam.csv', encoding='latin-1')[['v1', 'v2']]
    df.columns = ['label', 'message']

    # Encode labels: ham = 0, spam = 1
    df['label'] = df['label'].map({'ham': 0, 'spam': 1})

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        df['message'], df['label'], test_size=0.2, random_state=42)

    # TF-IDF vectorization
    vectorizer = TfidfVectorizer()
    X_train_tf = vectorizer.fit_transform(X_train)
    X_test_tf = vectorizer.transform(X_test)

    # Train model
    model = MultinomialNB()
    model.fit(X_train_tf, y_train)

    # Predict and evaluate
    y_pred = model.predict(X_test_tf)

    print("📊 Accuracy:", accuracy_score(y_test, y_pred))
    print("\n📃 Classification Report:\n", classification_report(y_test, y_pred))

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Ham', 'Spam'], yticklabels=['Ham', 'Spam'])
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    
    # Show or save the plot
    plt.tight_layout()
    plt.savefig("confusion_matrix.png")
    print("📁 Confusion matrix saved as 'confusion_matrix.png'.")

if __name__ == "__main__":
    main()
