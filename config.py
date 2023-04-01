from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "BQB1XZbsjMr0GDLwfuogDPwlRiRTfQCNgVKmdAJEmxPqpAaV85-u_fAZ5NSljM7wKeDpwc7A4BTLaGTEm8w3_dl0d4S2v81k_6uEaE4txLCnpnJ05gjZqp8ORArjdhNS3M5HO_DmUabmrO-2prVQvwq3q4m2F_h6W0gdWtld61-goE8DaFt2F4nGI1hNuc4l0IFSfsnnVMYKMCYnUk-a54evQ_F3-aK-lMBKMxjBHYM7kNu9ZzYoeHYuK6Mr8kDdiZKp7byxPykMiuIFJWPRSIoolGPcC1of58FE9T1MOAtjXLCEh7tc-9yHERPF9y2x_h7IDVDx4qrf4NXX167NVFXvAAAAAS6mjVwA")
BOT_TOKEN = getenv("BOT_TOKEN","5609007008:AAHjhJfYf6xAR28QvTqm5ZPJmllsG83sqTs")
BOT_NAME = getenv("BOT_NAME", "Deneme bot") 
API_ID = int(getenv("11919556"))
API_HASH = getenv("5609007008:AAHjhJfYf6xAR28QvTqm5ZPJmllsG83sqTs")
BOT_USERNAME = getenv("BOT_USERNAME", "@denenrobot")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
