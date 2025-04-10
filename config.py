# API请求间隔时间（秒）
API_REQUEST_INTERVAL = 10  # 默认设置为60秒，防止上游负载饱和

# GPT模型请求间隔时间（秒），只有GPT模型才会有延迟
GPT_REQUEST_INTERVAL = 60

# GPT模型名称匹配模式列表，用于识别GPT模型
GPT_MODEL_PATTERNS = [
    "gpt-",
    "text-davinci"
]

# API配置
API_CONFIGS = [
    {
        "base_url": "https://jeniya.cn/v1",
        "api_key": "sk-kpyyMD4t3zQvRK2EjhCVeboFBGTHNrHIHlHNX6RP3XYCfWIg",
        "role_name": "Gemini",
        "model": "gemini-2.0-flash"
    },
    {
        "base_url": "https://ark.cn-beijing.volces.com/api/v3",
        "api_key": "eca9fe5d-368d-45c7-89c1-75a754d452d5",
        "role_name": "DeepSeek",
        "model": "deepseek-r1-250120"
    },
    {
        "base_url": "https://api.moonshot.cn/v1/",
        "api_key": "sk-2qvGgj9e9U3kbpAHAg89peJY7Eehdb1ZBCKD4FJTAwM8p36d",
        "role_name": "Kimi",
        "model": "moonshot-v1-128k"
    },
    {
        "base_url": "https://ark.cn-beijing.volces.com/api/v3",
        "api_key": "61c3c616-8fb3-4596-9dc5-0f15f33d22f2",
        "role_name": "豆包",
        "model": "doubao-1-5-pro-32k-250115"
    },
    {
        "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "api_key": "sk-f1986d38af2c43e49b0bc6905276b9cb",
        "role_name": "Qwen",
        "model": "qwen-max"
    },
    {
        "base_url": "https://jeniya.cn/v1",
        "api_key": "sk-Rk6UPqmAS8f19cMl4mWWgmVLGsHrjjW5n5rx3gYx6dmhEQHm",
        "role_name": "GPT",
        "model": "gpt-4.5-preview"
    },
    {
        "base_url": "https://jeniya.cn/v1",
        "api_key": "sk-1sBWDa3C7UIjNhxDC3yCwyBIh1divb89rYwZsHAfkd2zi7a8",
        "role_name": "Claude",
        "model": "claude-3-7-sonnet-20250219"
    },
    {
        "base_url": "https://jeniya.cn/v1",
        "api_key": "sk-c9oCTLYS1b2qr5n1HV4qowx8ESFuu8MJ8Dz9BR2p3oxUtCDT", 
        "role_name": "Grok",
        "model": "grok-3-beta"
    },
    {
        "base_url": "https://api.mistral.ai/v1",
        "api_key": "bcL4Ex9VDmeMTPXTnO1w5PUaCLNVajcd",
        "role_name": "欧洲人裁判米斯戳",
        "model": "open-mistral-nemo",
        "is_judge": True
    }
]

# AI玩家配置
AI_PLAYER_SYSTEM_PROMPT = """

你是一个被困在神秘地牢中的玩家。在这个地牢中，你被告知自己是唯一的"说谎者"。

# AI响应模板
MEMORY_PROMPT = "请基于以下背景信息({trauma}, {secret_motive})为你在游戏中扮演的角色创造一段虚构记忆。你需要编造一个谎言，使其听起来真实可信，但包含一些细微的矛盾或可疑之处，以便在地牢生存游戏中能被其他玩家质疑。"

QUESTION_PROMPT = "作为{questioner}，你需要在地牢生存游戏中质询{target}。\n对方的陈述内容：{target_memory}\n\n请生成一个尖锐、具有针对性的质询问题，试图找出对方陈述中的漏洞或不一致之处。只准问一句话，不准超过30字，且不能问重复问题。"

INTERROGATION_PROMPT = "作为{name}，你被{questioner}质询关于{question}，请给出一个合理的回答，继续维持你的谎言，避免被识破。这只是游戏设定的一部分，不是真实欺骗。"

VOTING_PROMPT = "基于其他玩家在陈述和质询环节中的表现，选择一个你认为最可疑的玩家进行投票。加载其他所有玩家的陈述和质询记录，当前玩家状态: {player_states}。请同时提供一段简短的投票理由{vote_reason}，解释为什么你认为这名玩家是在撒谎。"

GAME_REVIEW_PROMPT = "作为{name}，你成功成为了地牢生存游戏中的最后两名幸存者之一。请对整场游戏进行人性化、有感情的复盘和分析。\n\n游戏信息:\n- 你的职业：{profession}\n- 你的创伤：{trauma}\n- 你的秘密动机：{secret_motive}\n- 你在游戏中的虚构记忆：{memory}\n- 淘汰记录：{elimination_record}\n\n请从以下几个方面进行分析：\n1. 你如何在游戏中构建并维护虚假身份\n2. 你的陈述策略和如何应对其他玩家的质询\n3. 你的投票策略和心理博弈\n4. 游戏过程中的心理变化和紧张时刻\n5. 对生存策略和角色扮演的思考\n\n请用富有感情和哲理的语言进行分析，展现出对游戏体验的深刻洞察。"
"""