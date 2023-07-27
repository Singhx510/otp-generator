import random

def generate_otp(length=6):
    """Generate a random OTP of the given length."""
    digits = "0123456789"
    otp = "".join(random.choice(digits) for _ in range(length))
    return otp

def verify_otp(otp_input, otp_generated):
    """Verify if the input OTP matches the generated OTP."""
    return otp_input == otp_generated

if __name__ == "__main__":
    # Example usage
    generated_otp = generate_otp()
    print("Generated OTP:", generated_otp)

    user_input = input("Enter the OTP you received: ")
    if verify_otp(user_input, generated_otp):
        print("OTP verified successfully!")
    else:
        print("Incorrect OTP. Verification failed.")
