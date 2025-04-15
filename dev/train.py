from config import config
from utilities import utils
from sklearn.model_selection import train_test_split

# Load and preprocess
df = utils.load_data(config.DATA_PATH)
df = utils.preprocess(df)

# Train-test split
X = df.drop(config.TARGET_COL, axis=1)
y = df[config.TARGET_COL]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=config.TEST_SIZE, random_state=config.RANDOM_STATE)

# Train and evaluate
model = utils.train_model(X_train, y_train)
score = utils.evaluate_model(model, X_test, y_test)

print(f"Model R² score: {score}")
