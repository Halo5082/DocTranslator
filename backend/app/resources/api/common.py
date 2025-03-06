# app/resources/api/common.py
from flask_restful import Resource

from app.utils.response import APIResponse
from app.models.setting import Setting


class SystemConfigResource(Resource):
    def get(self):
        """获取系统版本配置 [^6]"""
        try:
            version = Setting.get_version()
            return APIResponse.success({"version": version})

        except Exception as e:
            return APIResponse.error(
                message="服务器内部错误",
                code=500,
                errors=str(e)
            )
