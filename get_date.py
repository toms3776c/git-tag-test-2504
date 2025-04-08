from datetime import datetime

def get_current_datetime():
    """
    現在の日付と時間をYYYY-MM-DD HH:MM:SS形式で返す関数
    
    Returns:
        str: 現在の日付と時間（YYYY-MM-DD HH:MM:SS形式）
    """
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    print(f"現在の日時: {get_current_datetime()}")
