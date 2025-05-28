import sys
import asyncio
from telethon import TelegramClient
from telethon.tl.functions.account import ReportPeerRequest
from telethon.tl.types import (
    InputReportReasonSpam,
    InputReportReasonViolence,
    InputReportReasonPornography,
    InputReportReasonChildAbuse,
    InputReportReasonOther,
    InputReportReasonCopyright,
    InputReportReasonPersonalDetails,
    InputReportReasonIllegalDrugs
)

# Your Telegram API credentials
api_id = 123456  # Replace with your API ID
api_hash = 'your_api_hash'  # Replace with your API hash
phone_number = '+923XXXXXXXXX'  # Your phone number

# Report reasons
report_reasons = {
    1: ("Spam", InputReportReasonSpam()),
    2: ("Violence", InputReportReasonViolence()),
    3: ("Pornography", InputReportReasonPornography()),
    4: ("Child Abuse", InputReportReasonChildAbuse()),
    5: ("Illegal Drugs", InputReportReasonIllegalDrugs()),
    6: ("Personal Details", InputReportReasonPersonalDetails()),
    7: ("Copyright", InputReportReasonCopyright()),
    8: ("Other", InputReportReasonOther())
}

async def main():
    client = TelegramClient("multi_report_session", api_id, api_hash)
    await client.start(phone=phone_number)

    print("\n--- Telegram Multi-User Reporter ---\n")

    usernames_input = input("Enter usernames separated by comma (e.g. user1,user2): ")
    usernames = [u.strip() if u.strip().startswith("@") else "@" + u.strip() for u in usernames_input.split(",")]

    print("\nSelect a reason to report:")
    for k, (text, _) in report_reasons.items():
        print(f"{k}: {text}")

    while True:
        try:
            reason_choice = int(input("Enter reason number: "))
            if reason_choice in report_reasons:
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Enter a number.")

    while True:
        try:
            report_count = int(input("How many reports per user? "))
            break
        except ValueError:
            print("Enter a valid number.")

    for username in usernames:
        try:
            entity = await client.get_entity(username)
            print(f"\nReporting {username}...")

            for i in range(report_count):
                await client(ReportPeerRequest(
                    peer=entity,
                    reason=report_reasons[reason_choice][1],
                    message=f"Reported for {report_reasons[reason_choice][0]}"
                ))
                print(f"{username}: Report {i + 1} submitted.")
                await asyncio.sleep(2)

        except Exception as e:
            print(f"Error reporting {username}: {e}")

    print("\nReporting complete.")
    await client.disconnect()

if name == "main":
    asyncio.run(main())
