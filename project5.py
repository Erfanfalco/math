from sympy import *

# تعریف متغیرهای x، y و z به عنوان متغیرهای ورودی
x, y, z = symbols('x y z')

# تعریف دو منحنی داده شده
f1 = 3*x**2 + 2*y**2 + z**2 - 49
f2 = x**2 + y**2 - 2*z**2 - 10

# محاسبه بردار تناظری هر منحنی
grad_f1 = Matrix([diff(f1, x), diff(f1, y), diff(f1, z)])
grad_f2 = Matrix([diff(f2, x), diff(f2, y), diff(f2, z)])

# محاسبه بردار عمود به صفحه‌ی مشترک دو منحنی با ضرب داخلی بردارهای تناظری
normal_vector = grad_f1.cross(grad_f2)

# تعیین یکی از نقاط مشترک دو منحنی، برای استفاده در معادله صفحه‌ی قائم
# برای مثال، می‌توانیم از روش حل سیستم معادلات استفاده کنیم:
solution = solve((f1, f2), (x, y, z))

point = Matrix([solution[x], solution[y], solution[z]])

# محاسبه معادله صفحه‌ی قائم با استفاده از بردار عمود و یکی از نقاط مشترک دو منحنی
eq = normal_vector.dot(point) + simplify(f1.subs([(x, point[x]), (y, point[y]), (z, point[z])]))

# چاپ معادله صفحه‌ی قائم
print("معادله صفحه قائم بر دو منحنی:")
print(eq, "= 0")