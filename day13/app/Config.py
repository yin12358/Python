class Config(object):
    """项目共用的一些配置"""
    SECRET_KEY = '123456'


class DevelopmentConfig(Config):
    """开发环境"""
    DEBUG = True  # 打开测试

    # 数据库相关配置
    # 设置数据库的链接地址
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:python@localhost:3306/test?charset=utf8'
    # 关闭追踪数据库的修改
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """生产环境"""
    DEBUG = False  # 打开测试


APPCONFIG = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
