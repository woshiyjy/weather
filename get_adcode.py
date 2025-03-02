# 高德地图城市编码获取工具
# 用于获取中国主要城市的行政区划编码(adcode)
# adcode用于调用天气API时标识具体城市

import requests
import json

def get_city_adcode(city_name, max_retries=3):
    """获取城市的行政区划编码
    
    参数:
        city_name (str): 城市名称，如'北京市'、'上海市'
        max_retries (int): 最大重试次数，默认为3次
        
    返回:
        str/None: 成功返回城市的adcode，失败返回None
    """
    url = 'https://restapi.amap.com/v3/geocode/geo'
    params = {
        'key': '55cdad7d3ab1989cd17ab7e85e28725a',  # 高德地图API密钥
        'address': city_name
    }
    
    # 添加重试机制，提高请求成功率
    for attempt in range(max_retries):
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                # 检查返回数据的有效性
                if data.get('status') == '1' and data.get('geocodes') and len(data['geocodes']) > 0:
                    return data['geocodes'][0].get('adcode')
            if attempt < max_retries - 1:
                import time
                time.sleep(1)  # 在重试之前等待1秒，避免频繁请求
        except Exception as e:
            if attempt < max_retries - 1:
                import time
                time.sleep(1)  # 发生异常时也等待1秒后重试
            else:
                print(f'获取{city_name}的adcode时发生错误：{str(e)}')
    return None

def main():
    # 定义主要城市列表（包含省会城市和直辖市）
    cities = [
        '北京市', '上海市', '天津市', '重庆市',
        '石家庄市', '太原市', '呼和浩特市', '沈阳市',
        '长春市', '哈尔滨市', '南京市', '杭州市',
        '合肥市', '福州市', '南昌市', '济南市',
        '郑州市', '武汉市', '长沙市', '广州市',
        '南宁市', '海口市', '成都市', '贵阳市',
        '昆明市', '拉萨市', '西安市', '兰州市',
        '西宁市', '银川市', '乌鲁木齐市'
    ]
    
    # 用字典存储城市和对应的adcode
    city_adcodes = {}
    
    # 遍历城市列表获取adcode
    for city in cities:
        adcode = get_city_adcode(city)
        if adcode:
            city_adcodes[adcode] = city
            print(f'{city}: {adcode}')
        else:
            print(f'无法获取{city}的adcode')
    
    # 将结果保存为JSON文件，便于后续使用
    with open('city_adcodes.json', 'w', encoding='utf-8') as f:
        json.dump(city_adcodes, f, ensure_ascii=False, indent=4)
    
    print('\n城市adcode信息已保存到city_adcodes.json文件中')

if __name__ == '__main__':
    main()