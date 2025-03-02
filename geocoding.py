# 高德地图地理编码和逆地理编码API调用模块
# 用于实现地址与经纬度之间的相互转换，以及获取区域编码等信息

import requests
import json

def geocode(address):
    """地理编码：将地址转换为经纬度和adcode
    
    参数:
        address (str): 需要转换的地址字符串
        
    返回:
        dict: 包含转换结果的字典
            - status: 转换是否成功
            - location: 经纬度坐标
            - adcode: 区域编码
            - formatted_address: 标准化地址
            - level: 匹配级别
    """
    url = 'https://restapi.amap.com/v3/geocode/geo'
    params = {
        'key': '55cdad7d3ab1989cd17ab7e85e28725a',  # 高德地图API密钥
        'address': address
    }
    
    try:
        # 发送GET请求获取地理编码信息
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            # 检查返回数据的有效性
            if data.get('status') == '1' and data.get('geocodes') and len(data['geocodes']) > 0:
                result = data['geocodes'][0]
                return {
                    'status': True,
                    'location': result.get('location', ''),  # 经纬度
                    'adcode': result.get('adcode', ''),     # 区域编码
                    'formatted_address': result.get('formatted_address', ''),  # 格式化地址
                    'level': result.get('level', '')        # 匹配级别
                }
        return {'status': False, 'message': '地理编码请求失败'}
    except Exception as e:
        return {'status': False, 'message': f'发生错误: {str(e)}'}

def reverse_geocode(location):
    """逆地理编码：将经纬度转换为地址和adcode
    
    参数:
        location (str): 经纬度坐标，格式为"经度,纬度"
        
    返回:
        dict: 包含转换结果的字典
            - status: 转换是否成功
            - formatted_address: 标准化地址
            - adcode: 区域编码
            - city: 城市名称
            - district: 区县名称
    """
    url = 'https://restapi.amap.com/v3/geocode/regeo'
    params = {
        'key': '55cdad7d3ab1989cd17ab7e85e28725a',  # 高德地图API密钥
        'location': location,  # 经度,纬度
        'extensions': 'base'   # 返回基本地址信息
    }
    
    try:
        # 发送GET请求获取逆地理编码信息
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            # 检查返回数据的有效性
            if data.get('status') == '1' and data.get('regeocode'):
                result = data['regeocode']
                address_component = result.get('addressComponent', {})
                return {
                    'status': True,
                    'formatted_address': result.get('formatted_address', ''),  # 格式化地址
                    'adcode': address_component.get('adcode', ''),  # 区域编码
                    'city': address_component.get('city', ''),      # 城市名称
                    'district': address_component.get('district', '')  # 区县名称
                }
        return {'status': False, 'message': '逆地理编码请求失败'}
    except Exception as e:
        return {'status': False, 'message': f'发生错误: {str(e)}'}

def main():
    # 测试地理编码功能
    print('\n=== 测试地理编码 ===')
    test_addresses = ['北京市朝阳区', '上海市浦东新区', '广州市天河区']
    for address in test_addresses:
        result = geocode(address)
        if result['status']:
            print(f'\n地址: {address}')
            print(f'经纬度: {result["location"]}')
            print(f'区域编码: {result["adcode"]}')
            print(f'格式化地址: {result["formatted_address"]}')
            print(f'匹配级别: {result["level"]}')
        else:
            print(f'\n地址 {address} 查询失败: {result["message"]}')
    
    # 测试逆地理编码功能
    print('\n=== 测试逆地理编码 ===')
    test_locations = ['116.397428,39.90923', '121.473701,31.230416']
    for location in test_locations:
        result = reverse_geocode(location)
        if result['status']:
            print(f'\n经纬度: {location}')
            print(f'格式化地址: {result["formatted_address"]}')
            print(f'区域编码: {result["adcode"]}')
            print(f'城市: {result["city"]}')
            print(f'区县: {result["district"]}')
        else:
            print(f'\n经纬度 {location} 查询失败: {result["message"]}')

if __name__ == '__main__':
    main()