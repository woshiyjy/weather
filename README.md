# 全国主要城市天气信息查询系统

## 项目简介
这是一个基于高德地图API的全国主要城市天气信息查询系统，支持实时天气数据展示。系统覆盖了全国所有省会城市和直辖市，为用户提供准确、及时的天气信息服务。

## 功能特点
- 实时天气数据展示
- 主要城市天气信息汇总
- 温度分级显示
- 风向和风力等级展示
- 自动数据更新（每分钟）

## 技术架构
- 前端：HTML5、CSS3、JavaScript
- UI框架：Font Awesome 图标库
- API：高德地图天气API
- 数据展示：响应式布局设计

## 数据指标
系统提供以下天气相关指标：
- 天气状况
- 实时温度
- 风向信息
- 风力等级
- 空气湿度

## 使用方法
1. 克隆项目到本地
```bash
git clone [项目地址]
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 配置API密钥
在`test_weather_api.py`文件中配置您的高德地图API密钥：
```python
base_params = {
    'key': '您的API密钥',
    'extensions': 'base'
}
```

4. 运行项目
- 运行Python脚本查看命令行输出：
```bash
python test_weather_api.py
```
- 或者直接在浏览器中打开`index.html`查看网页版展示

## 注意事项
- 请确保您有有效的高德地图API密钥
- 建议使用现代浏览器访问网页版
- API请求可能会有频率限制，请合理使用

## 贡献指南
欢迎提交问题和改进建议，您可以：
1. 提交Issue报告问题
2. 提交Pull Request贡献代码
3. 完善文档和使用说明

## 许可证
MIT License