# API Contract User Profile

    **Endpoint:** /api/v1/profile
    **Method:** GET
    **Response Body (JSON):**
    {
      "id": 1,
      "username": "mahasiswa_sd",
      "email": "mhs@univ.ac.id",
      "avatar_url": "https://image.com/avatar.png"
    }

# API Contract Login

**Endpoint:** /api/v1/login
**Method:** POST
**Request Body (JSON):**
{
"username": "mahasiswa_sd",
"password": "your_password"
}
**Response Body (JSON):**
{
"status": "success",
"token": "jwt_example_token_123"
}
