ckstyle-pm
==========

Plugin Manager for CKstyle
## 简介

欢迎来到CKstyle的插件管理中心

### 插件安装

通过 `ckstyle install/get/add pluginName` 即可安装规则插件

通过 `ckstyle installcmd/getcmd/addcmd commandName` 即可安装ckstyle的子命令插件

### 插件开发

插件主要分为规则插件和子命令插件两种，分别放置在 `plugins` 和 `commands` 目录下

#### 规则插件的开发

1、规则插件请放置在 `ckstyle-pm/plugins` 目录下

2、规则插件名的小写形式，即为子目录名，例如插件 demo 放置在 `ckstyle-pm/plugins/demo` 目录下，而命令行以 `ckstyle get demo` 来获取

3、插件类所在文件名为 `index.py`，此文件中的必须包含插件类名称为：`PluginClass`，而且此类必须继承自特定的 `CKstyle检查类` 。示例请参见<a href="https://github.com/wangjeaf/ckstyle-pm/blob/master/plugins/demo/index.py">demo plugin</a>

规则插件类的详细编写规则，请参见 <a href="https://github.com/wangjeaf/CSSCheckStyle#plugin-development" target="_blank">CKstyle的官方插件开发文档</a>

#### 子命令插件的开发

目前ckstyle已经通过子命令的方式来进行各种操作，同时允许插件扩展ckstyle的子命令。

1、子命令插件请放置在 `ckstyle-pm/commands` 目录下

2、插件名称的小写形式，即为子目录名，例如democmd放置在 `ckstyle-pm/commands/democmd` 目录下，而命令行以 `ckstyle getcmd democmd` 的方式来安装到本地

3、插件类所在的文件名为 `index.py`，此文件中必须包含一个 `doCommand` 方法，进行主要的命令操作

具体示例请参见<a href="https://github.com/wangjeaf/ckstyle-pm/blob/master/commands/democmd/index.py">demo command</a>