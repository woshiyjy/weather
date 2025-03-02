import requests
import json

def get_city_adcode(city_name, max_retries=3):
    url = 'https://restapi.amap.com/v3/geocode/geo'
    params = {
        'key': '55cdad7d3ab1989cd17ab7e85e28725a',
        'address': city_name
    }
    
    for attempt in range(max_retries):
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == '1' and data.get('geocodes') and len(data['geocodes']) > 0:
                    return data['geocodes'][0].get('adcode')
            if attempt < max_retries - 1:
                import time
                time.sleep(1)  # 在重试之前等待1秒
        except Exception as e:
            if attempt < max_retries - 1:
                import time
                time.sleep(1)  # 在重试之前等待1秒
            else:
                print(f'获取{city_name}的adcode时发生错误：{str(e)}')
    return None

def main():
    # 主要城市列表（省会城市和直辖市）
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
    
    # 存储城市和对应的adcode
    city_adcodes = {}
    
    # 获取每个城市的adcode
    for city in cities:
        adcode = get_city_adcode(city)
        if adcode:
            city_adcodes[adcode] = city
            print(f'{city}: {adcode}')
        else:
            print(f'无法获取{city}的adcode')
    
    # 将结果保存为JSON文件
    with open('city_adcodes.json', 'w', encoding='utf-8') as f:
        json.dump(city_adcodes, f, ensure_ascii=False, indent=4)
    
    print('\n城市adcode信息已保存到city_adcodes.json文件中')

if __name__ == '__main__':
    main()