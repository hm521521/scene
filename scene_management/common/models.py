from django.conf.global_settings import MEDIA_ROOT
from django.contrib.auth.hashers import make_password
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
def upload_to(instance, filename):
    return '/'.join([MEDIA_ROOT, instance.id, filename])

class users(models.Model):
    username=models.CharField(max_length=50,verbose_name='用户名')
    password=models.CharField(max_length=200,verbose_name='密码')
    phonenumber=models.CharField(max_length=50,verbose_name='电话')
    groupid=models.CharField(max_length=50,choices=((0,'管理员'),(1,'用户')),verbose_name='用户类型')

    def save(self,*args,**kwargs):
        self.password=make_password(self.password, None, 'pbkdf2_sha256')
        super(users,self).save(*args,**kwargs)

class sources(models.Model):
    # id=models.AutoField(primary_key=True)
    file=models.FileField(upload_to=upload_to, verbose_name='资源保存的路径')
    name=models.CharField(max_length=50,verbose_name='资源名称')
    unique = models.UUIDField(verbose_name='资源的唯一标识码')
    type = models.IntegerField(choices=((0, '图片'), (1, '视频')), verbose_name='资源类型')
    mgrid = models.ForeignKey(users, on_delete=models.PROTECT, verbose_name='录入资源的管理员id')
    # size = models.IntegerField(verbose_name='上传资源的大小')


class artdata(models.Model):
    # 默认情况下，模型自动创建主键id字段，也可以显示定义主键
    # id = models.AutoField(primary_key=True)
    # unique = models.UUIDField(verbose_name='资源的唯一标识码')
    # picname = models.CharField(max_length=50, verbose_name='资源名称')
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    # fileurl = models.FilePathField(upload_to=upload_to, verbose_name='资源保存路径')
    sources_id=models.ForeignKey(sources,on_delete=models.PROTECT,verbose_name='资源表中的编号')

class IP(models.Model):
    IP_name = models.CharField(max_length=50, verbose_name='IP名称')
    fileurl = models.ImageField(upload_to=upload_to, verbose_name='IP保存路径')
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    min_age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    max_age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

class sta_analyze(models.Model):
    # id = models.AutoField(primary_key=True)
    mean = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    equilibrum = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    dis_url = models.CharField(max_length=250, verbose_name='亮度曲线路径')
    sources_id = models.ForeignKey(sources, on_delete=models.PROTECT, verbose_name='保存在sources表里的id')
    sta_thres=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(255)], verbose_name='静态阈值')

class dyn_analyze(models.Model):
    # id = models.AutoField(primary_key=True)
    sources_id = models.ForeignKey(sources, on_delete=models.PROTECT, verbose_name='保存在sources表里的id')
    strobnum=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(255)], verbose_name='频闪次数')
    peak=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)], verbose_name='峰值亮度')
    dis_url=models.CharField(max_length=250, verbose_name='动态亮度分布曲线路径')

class distribute(models.Model):
    dis_fun = models.CharField(max_length=200,choices=((0, 'sigmoid'), (1, 'Gaussian')), verbose_name='分布函数')
    min = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name='最小取值')
    max = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name='最大取值')
    # parameters = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(255)], verbose_name='分布参数')
    centre=models.FloatField()
    shape=models.FloatField()



class sta_bright_indic(distribute):
    sta_bright=models.CharField(max_length=200,choices=(('mean','平均亮度'),('equilibrium','亮度分布均匀度')),verbose_name='静态亮度选项')
    sta_thres=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(255)], verbose_name='静态亮度阈值')

class dyn_bright_indic(distribute):
    dyn_bright=models.CharField(max_length=200,choices=(('strob_num','频闪次数'),('peak','亮度峰值')))
    bright_diff=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(255)],verbose_name='亮度差值')
    span=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(300)],verbose_name='计算动态亮度的时长')


class chorma_indic(distribute):
    chorma=models.CharField(max_length=200,choices=(('constast','对比色'),('adjacent','邻近色'),('complement','互补色'),('analogous','类似色'),
                                    ('harmonious','色彩和谐度'),('temrature','色温'),('hue','色差')),verbose_name='彩度选项')


class indiactors(models.Model):
    sta_bright = models.ForeignKey(sta_bright_indic,on_delete=models.PROTECT,verbose_name='静态亮度指标')
    dyn_bright = models.ForeignKey(dyn_bright_indic,on_delete=models.PROTECT,verbose_name='动态亮度指标')
    chorma = models.ForeignKey(chorma_indic,on_delete=models.PROTECT,verbose_name='彩度指标')
    weight_sta = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(1)],verbose_name='静态亮度权重')
    weight_chr = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(1)],verbose_name='彩度权重')
    # weight_dyn=models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(1)],verbose_name='动态亮度权重')
    radius = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(100)],verbose_name='评估半径')

class scores(models.Model):
    sources_id=models.ForeignKey(sources,on_delete=models.PROTECT,verbose_name='资源表的编号')
    sta_score=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)],verbose_name='静态亮度的评分')
    dyn_score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name='动态亮度的评分')
    chr_score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name='彩度的评分')
    indicator_id=models.ForeignKey(indiactors,on_delete=models.PROTECT,verbose_name='选择的指标编号')
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name='综合评分')

class cameras(models.Model):
    name=models.CharField(max_length=50,verbose_name='摄像头名称')
    IP=models.CharField(max_length=200,verbose_name='摄像头的IP地址')
    username=models.CharField(max_length=50,verbose_name='摄像头的用户名')
    password=models.CharField(max_length=200,verbose_name='密码')
    port=models.CharField(max_length=200,verbose_name='端口号')

class chr_analyze(models.Model):
    sources_id=models.ForeignKey(sources,on_delete=models.PROTECT,verbose_name='资源编号')
    contrat_num=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2000)], verbose_name='对比色的对数')
    adajacent_num = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2000)], verbose_name='邻近色的对数')
    complementary_num = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2000)], verbose_name='互补色的对数')
    analogous_num = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2000)], verbose_name='类似色的对数')
    con_curve = models.CharField(max_length=250, verbose_name='对比色分布曲线路径')
    adj_curve= models.CharField(max_length=250, verbose_name='邻近色分布曲线路径')
    com_curve = models.CharField(max_length=250, verbose_name='互补色分布曲线路径')
    ana_curve= models.CharField(max_length=250, verbose_name='类似色分布曲线路径')
    colors_curve= models.CharField(max_length=250, verbose_name='色彩分布图路径')
    harmonious=models.IntegerField(verbose_name='色彩和谐度')
    temperature = models.CharField(max_length=250, verbose_name='色温曲线路径')
    hue_curve = models.CharField(max_length=250, verbose_name='色调曲线路径')

class IPattraction(models.Model):
    sources_id=models.ForeignKey(sources,on_delete=models.PROTECT,verbose_name='资源编号')
    total=models.IntegerField(verbose_name='IP的个数')
    IPid=models.ManyToManyField(IP,verbose_name='IP的编号')
    attraction_url=models.CharField(max_length=250, verbose_name='吸引力曲线路径')

