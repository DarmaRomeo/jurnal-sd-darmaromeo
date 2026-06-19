# Database Schema

## Tabel: Users

Menyimpan data otentikasi pengguna.

- id (Integer, Primary Key)
- username (Varchar)
- email (Varchar)
- password (Varchar)

## Tabel: Profiles

Menyimpan informasi tambahan profil pengguna.

- id (Integer, Primary Key)
- user_id (Integer, Foreign Key)
- avatar_url (Varchar)
