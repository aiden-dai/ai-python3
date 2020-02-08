import random

random.seed(5)

a = random.randint(5, 10)  # random integer from 5 to 10
b = random.random()  # random float from 0 to 1
c = random.uniform(5, 10)  # random float from 5 to 10

print(a)  # 9
print(b)  # 
print(c)

x = ['Tom', 'John', 'Kate']
d = random.choice(x)
print(d)

random.shuffle(x)
print(x)

y = random.sample('abcdefghijk', 5)
print(y)


# random.normalvariate(mu, sigma),  mu is the mean, and sigma is the standard deviation
z1 = random.normalvariate(0, 1)  # Normal distribution.
print(z1)

# random.gauss(mu, sigma), mu is the mean, and sigma is the standard deviation. 
z2 = random.gauss(0, 1)
print(z2)