import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

np.random.seed(0)
x=2.5*np.random.randn(100)+1.5
res=0.5*np.random.randn(100)
y=2+0.3*x+res

df=pd.DataFrame({'x':x, 'y':y})

plt.scatter(df['x'], df['y'], color='blue', label='Data points')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter plot of x vs y')
plt.legend()
plt.show()


x=df[['x']]
y=df['y']
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.2, random_state=0)

model=LinearRegression()
model.fit(x_train, y_train)

y_pred=model.predict(x_test)

print('기울기 (slope):', model.coef_[0])
print('절편 (Intercept):', model.intercept_)
print('평균 제곱 오차 (MSE):', mean_squared_error(y_test, y_pred))
print('결정 계수 (R^2):', r2_score(y_test, y_pred))

plt.scatter(x_test, y_test, color='blue', label='Actual data')
plt.plot(x_test, y_pred, color='red', linewidth=2, label='Fitted line')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()