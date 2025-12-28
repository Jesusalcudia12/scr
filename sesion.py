from pyrogram import Client

api_id = input("36863635: ")
api_hash = input("eaad5e9e1f20e047daee4997e88814d6: ")

with Client(":memory:", api_id=api_id, api_hash=api_hash) as app:
    print("\nTu SESSION_STRING es:\n")
    print(app.export_session_string())
