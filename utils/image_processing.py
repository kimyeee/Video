# coding: utf-8
import os

import requests
from io import BytesIO
from rest_framework import exceptions
from PIL import Image, ImageDraw, ImageFont
import logging
import uuid

from CpBackend.settings import MEDIA_ROOT

logger = logging.getLogger("django")


class ImageProcessing:
    @staticmethod
    def process_two(base_img_url, head_img_url, nickname, qrcode_img):
        """
        生成带二维码的图片
        :param base_img_url: 报告背景图片
        :param head_img_url: 用户微信头像远程访问地址
        :param nickname: 用户昵称
        :param qrcode_img:二维码图片
        :return: 报告结果保存在服务器上的地址
        """
        if not os.path.exists(base_img_url):
            logger.info('File %s Not Exist' % base_img_url)
            raise exceptions.ValidationError('底图不存在')
        image = Image.open(base_img_url)
        # 将nickname绘画到指定区域
        font_path = os.path.abspath(os.path.join(MEDIA_ROOT, "fonts/PINGFANG REGULAR.TTF"))
        font = ImageFont.truetype(font_path, 28)
        draw = ImageDraw.Draw(image)
        draw.text((370, 100), nickname, fill=(0, 0, 0), font=font)
        # 对远程获取的头像进行处理
        html_res = requests.get(head_img_url, verify=False)
        local_head_image = Image.open(BytesIO(html_res.content))
        local_head_image.thumbnail((90, 90))
        result = ImageProcessing.draw_circle_avatar(local_head_image, image, (270, 70))
        # 加入二维码
        qrcode_image = Image.open(qrcode_img)
        qrcode_image.thumbnail((200, 200))
        result.paste(qrcode_image, (270, 770))
        relative_path = 'images/result/' + str(uuid.uuid4()) + '.jpg'
        if not os.path.isdir(os.path.abspath(os.path.join(MEDIA_ROOT, 'images/result/'))):
            os.makedirs(os.path.abspath(os.path.join(MEDIA_ROOT, 'images/result/')))
        image_save_url = os.path.abspath(os.path.join(MEDIA_ROOT, relative_path))
        result.save(image_save_url)
        return relative_path

    @staticmethod
    def process_one(base_img_url, head_img_url, nickname, code):
        """
        生成分享图片（不带二维码）
        :param base_img_url: 报告背景图片
        :param head_img_url: 用户微信头像远程访问地址
        :param nickname: 用户昵称
        :param code:二维码图片
        :return: 报告结果保存在服务器上的地址
        """
        if not os.path.exists(base_img_url):
            logger.info('File %s Not Exist' % base_img_url)
            raise exceptions.ValidationError('底图不存在')
        image = Image.open(base_img_url)
        # 将nickname绘画到指定区域
        font_path = os.path.abspath(os.path.join(MEDIA_ROOT, "fonts/PINGFANG REGULAR.TTF"))
        font = ImageFont.truetype(font_path, 28)
        draw = ImageDraw.Draw(image)
        draw.text((370, 100), nickname, fill=(0, 0, 0), font=font)
        # 将分享码绘画到指定区域
        font_path_bold = os.path.abspath(os.path.join(MEDIA_ROOT, "fonts/jiacu.ttf"))
        font = ImageFont.truetype(font_path_bold, 27)
        draw.text((491, 971), code, fill=(0, 0, 0), font=font)
        # 对远程获取的头像进行处理
        html_res = requests.get(head_img_url, verify=False)
        local_head_image = Image.open(BytesIO(html_res.content))
        local_head_image.thumbnail((90, 90))
        result = ImageProcessing.draw_circle_avatar(local_head_image, image, (270, 70))
        relative_path = 'images/result/' + str(uuid.uuid4()) + '.jpg'
        if not os.path.isdir(os.path.abspath(os.path.join(MEDIA_ROOT, 'images/result/'))):
            os.makedirs(os.path.abspath(os.path.join(MEDIA_ROOT, 'images/result/')))
        image_save_url = os.path.abspath(os.path.join(MEDIA_ROOT, relative_path))
        result.save(image_save_url)
        return relative_path

    @staticmethod
    def draw_circle_avatar(head_image, background, location):
        """
        将头像变成圆形绘制在背景图片上，然后将合成的图片对象返回
        """
        # 如果头像的色彩度是L，则需要进行转换，否则粘贴图片报异常
        if head_image.mode == 'L' or head_image.mode == 'CMYK':
            head_image = head_image.convert('RGB')
        big_size = (head_image.size[0] * 3, head_image.size[1] * 3)
        # 遮罩对象
        mask = Image.new('L', big_size, 0)
        draw = ImageDraw.Draw(mask)
        # 画椭圆的方法
        draw.ellipse((0, 0) + big_size, fill=255)
        mask = mask.resize(head_image.size, Image.ANTIALIAS)
        head_image.putalpha(mask)
        background.paste(head_image, location, head_image)
        return background
