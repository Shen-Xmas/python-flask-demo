from enum import Enum


class MsgDesc(Enum):
    """
    HTTP status说明
    200 OK  请求成功。一般用于GET与POST请求
    201 Created  表已创建。成功请求并创建了新的资源
    202 Accepted  已接受。已经接受请求，但未处理完成
    203 Non-Authoritative Information  非授权信息。请求成功。但返回的meta信息不在原始的服务器，而是一个副本
    204 No Content 无内容。服务器成功处理，但未返回内容。在未更新网页的情况下，可确保浏览器继续显示当前文档
    400 Bad Request  客户端请求的语法错误，服务器无法理解
    401 Unauthorized  请求要求用户的身份认证
    402 Payment Required  保留，将来使用
    403 Forbidden  服务器理解请求客户端的请求，但是拒绝执行此请求
    404 Not Found  服务器无法根据客户端的请求找到资源（网页）。通过此代码，网站设计人员可设置"您所请求的资源无法找到"的个性页面
    405 Method Not Allowed  客户端请求中的方法被禁止
    406 Not Acceptable  服务器无法根据客户端请求的内容特性完成请求
    407 Proxy Authentication Required  请求要求代理的身份认证，与401类似，但请求者应当使用代理进行授权
    408 Request Time-out  服务器等待客户端发送的请求时间过长，超时
    409 Conflict  服务器完成客户端的 PUT 请求时可能返回此代码，服务器处理请求时发生了冲突
    410 Gone  客户端请求的资源已经不存在。410不同于404，如果资源以前有现在被永久删除了可使用410代码，
              网站设计人员可通过301代码指定资源的新位置
    411 Length Required  服务器无法处理客户端发送的不带Content-Length的请求信息
    412 Precondition Failed  客户端请求信息的先决条件错误
    413 Request Entity Too Large  由于请求的实体过大，服务器无法处理，因此拒绝请求。为防止客户端的连续请求，服务器可能会关闭连接。
                                  如果只是服务器暂时无法处理，则会包含一个Retry-After的响应信息
    414 Request-URI Too Large  请求的URI过长（URI通常为网址），服务器无法处理
    415 Unsupported Media Type  服务器无法处理请求附带的媒体格式
    416 Requested range not satisfiable  客户端请求的范围无效
    417 Expectation Failed  服务器无法满足Expect的请求头信息
    500 Internal Server Error  服务器内部错误，无法完成请求
    501 Not Implemented  服务器不支持请求的功能，无法完成请求
    502 Bad Gateway  作为网关或者代理工作的服务器尝试执行请求时，从远程服务器接收到了一个无效的响应
    503 Service Unavailable  由于超载或系统维护，服务器暂时的无法处理客户端的请求。延时的长度可包含在服务器的Retry-After头信息中
    504 Gateway Time-out  充当网关或代理的服务器，未及时从远端服务器获取请求
    505 HTTP Version not supported  服务器不支持请求的HTTP协议的版本，无法完成处理
    """
    # 操作类
    h_200101 = "查询操作执行成功。"

    h_201101 = "表单提交成功/数据更新成功。"

    # 参数类


    # 权限类


    # 程序异常类

