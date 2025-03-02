import requests
import json
from prettytable import PrettyTable

def get_weather():
    """获取全国主要城市的天气信息
    
    该函数会获取所有省会城市和直辖市的实时天气信息，
    包括天气状况、温度、风向、风力、湿度等
    """
    # 主要城市列表（省会城市和直辖市）
    cities = {
        '110000': '北京市',
        '310000': '上海市',
        '120000': '天津市',
        '500000': '重庆市',
        '130100': '河北省石家庄市',
        '140100': '山西省太原市',
        '150100': '内蒙古自治区呼和浩特市',
        '210100': '辽宁省沈阳市',
        '220100': '吉林省长春市',
        '230100': '黑龙江省哈尔滨市',
        '320100': '江苏省南京市',
        '330100': '浙江省杭州市',
        '340100': '安徽省合肥市',
        '350100': '福建省福州市',
        '360100': '江西省南昌市',
        '370100': '山东省济南市',
        '410100': '河南省郑州市',
        '420100': '湖北省武汉市',
        '430100': '湖南省长沙市',
        '440100': '广东省广州市',
        '450100': '广西壮族自治区南宁市',
        '460100': '海南省海口市',
        '510100': '四川省成都市',
        '520100': '贵州省贵阳市',
        '530100': '云南省昆明市',
        '540100': '西藏自治区拉萨市',
        '610100': '陕西省西安市',
        '620100': '甘肃省兰州市',
        '630100': '青海省西宁市',
        '640100': '宁夏回族自治区银川市',
        '650100': '新疆维吾尔自治区乌鲁木齐市'
    }
    
    # 创建表格用于展示数据
    table = PrettyTable()
    table.field_names = ["城市", "天气", "温度(℃)", "风向", "风力", "湿度(%)"]
    
    # API参数设置
    base_params = {
        'key': '55cdad7d3ab1989cd17ab7e85e28725a',  # 高德地图API密钥
        'extensions': 'base'  # 返回实时天气数据
    }
    
    url = 'https://restapi.amap.com/v3/weather/weatherInfo'
    
    # 遍历所有城市获取天气信息
    for city_code, city_name in cities.items():
        params = base_params.copy()
        params['city'] = city_code
        
        try:
            # 发送API请求获取天气数据
            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == '1' and data.get('lives') and len(data['lives']) > 0:
                    weather = data['lives'][0]
                    table.add_row([
                        city_name,  # 城市名称
                        weather.get('weather', '未知'),  # 天气状况
                        weather.get('temperature', '未知'),  # 温度
                        weather.get('winddirection', '未知'),  # 风向
                        weather.get('windpower', '未知') + '级',  # 风力
                        weather.get('humidity', '未知')  # 湿度
                    ])
                else:
                    table.add_row([city_name, '获取失败', '-', '-', '-', '-'])
            else:
                table.add_row([city_name, '请求失败', '-', '-', '-', '-'])
        except Exception as e:
            table.add_row([city_name, f'错误: {str(e)}', '-', '-', '-', '-'])
    
    # 设置表格样式并打印
    table.align = 'l'  # 左对齐
    print('\n全国主要城市天气信息：')
    print(table)

if __name__ == '__main__':
    get_weather()