class User:
    def __init__(self, name, age, phoneNumber, paymentMethod, email=None):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must not be empty.")
        if isinstance(age, bool) or not isinstance(age, int) or age <= 0:
            raise ValueError("Age must be a positive integer.")
        if not isinstance(phoneNumber, str) or not phoneNumber.strip():
            raise ValueError("Phone number must not be empty.")
        if not isinstance(paymentMethod, str) or not paymentMethod.strip():
            raise ValueError("Payment method must not be empty.")
        if email is not None and (not isinstance(email, str) or not email.strip()):
            raise ValueError("Email must not be empty when provided.")

        self.name = name.strip()
        self.age = age
        self.phoneNumber = phoneNumber.strip()
        self.paymentMethod = paymentMethod.strip()
        self.email = email.strip() if email is not None else None

    def __str__(self):
        email_text = f", Email: {self.email}" if self.email else ""
        return (
            f"User: {self.name}, Age: {self.age}, Phone: {self.phoneNumber}"
            f"{email_text}, Payment: {self.paymentMethod}"
        )


if __name__ == "__main__":
    u1 = User("Hripsime", 22, "+37491247141", "vtb", email="miban@gmail.com")
    print(u1)
