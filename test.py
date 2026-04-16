import google.generativeai as genai
import os

# 將你提供的 API Key 填入此處
# 注意：你提供的這串字元看起來是不完整的，正式的 Google API Key 通常有 39 個字元
API_KEY = "AIzaSyBX3pPWwjU65Tc_wzOqjpzP4uYXg32los4" 

# 設定 API Key
genai.configure(api_key=API_KEY)

def list_available_models():
    try:
        print("正在查詢可用的模型清單...\n")
        print("-" * 50)
        
        # 取得所有可用模型
        for model in genai.list_models():
            print(f"模型名稱: {model.name}")
            print(f"顯示名稱: {model.display_name}")
            print(f"支援的方法: {', '.join(model.supported_generation_methods)}")
            print(f"簡介: {model.description}")
            print("-" * 50)
            
    except Exception as e:
        print(f"發生錯誤，請確認你的 API Key 是否正確或完整：\n{e}")

if __name__ == "__main__":
    list_available_models()