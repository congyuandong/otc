/*
 Navicat MySQL Data Transfer

 Source Server         : localhost
 Source Server Version : 50163
 Source Host           : localhost
 Source Database       : otc

 Target Server Version : 50163
 File Encoding         : utf-8

 Date: 10/15/2014 14:02:22 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `auth_group_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=43 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `auth_permission`
-- ----------------------------
BEGIN;
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry'), ('2', 'Can change log entry', '1', 'change_logentry'), ('3', 'Can delete log entry', '1', 'delete_logentry'), ('4', 'Can add permission', '2', 'add_permission'), ('5', 'Can change permission', '2', 'change_permission'), ('6', 'Can delete permission', '2', 'delete_permission'), ('7', 'Can add group', '3', 'add_group'), ('8', 'Can change group', '3', 'change_group'), ('9', 'Can delete group', '3', 'delete_group'), ('10', 'Can add user', '4', 'add_user'), ('11', 'Can change user', '4', 'change_user'), ('12', 'Can delete user', '4', 'delete_user'), ('13', 'Can add content type', '5', 'add_contenttype'), ('14', 'Can change content type', '5', 'change_contenttype'), ('15', 'Can delete content type', '5', 'delete_contenttype'), ('16', 'Can add session', '6', 'add_session'), ('17', 'Can change session', '6', 'change_session'), ('18', 'Can delete session', '6', 'delete_session'), ('19', 'Can add 市场', '7', 'add_region'), ('20', 'Can change 市场', '7', 'change_region'), ('21', 'Can delete 市场', '7', 'delete_region'), ('22', 'Can add otc', '8', 'add_otc'), ('23', 'Can change otc', '8', 'change_otc'), ('24', 'Can delete otc', '8', 'delete_otc'), ('25', 'Can add 市场容量', '9', 'add_industry'), ('26', 'Can change 市场容量', '9', 'change_industry'), ('27', 'Can delete 市场容量', '9', 'delete_industry'), ('28', 'Can add 市场容量指数', '10', 'add_industry_index'), ('29', 'Can change 市场容量指数', '10', 'change_industry_index'), ('30', 'Can delete 市场容量指数', '10', 'delete_industry_index'), ('31', 'Can add OTC公告', '11', 'add_otc_new'), ('32', 'Can change OTC公告', '11', 'change_otc_new'), ('33', 'Can delete OTC公告', '11', 'delete_otc_new'), ('34', 'Can add OTC研告', '12', 'add_otc_study'), ('35', 'Can change OTC研告', '12', 'change_otc_study'), ('36', 'Can delete OTC研告', '12', 'delete_otc_study'), ('37', 'Can add 近期热门证券', '13', 'add_otc_hot'), ('38', 'Can change 近期热门证券', '13', 'change_otc_hot'), ('39', 'Can delete 近期热门证券', '13', 'delete_otc_hot'), ('40', 'Can add 基础数据', '14', 'add_otc_base'), ('41', 'Can change 基础数据', '14', 'change_otc_base'), ('42', 'Can delete 基础数据', '14', 'delete_otc_base');
COMMIT;

-- ----------------------------
--  Table structure for `auth_user`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `auth_user`
-- ----------------------------
BEGIN;
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$12000$OGVhLW8spoL9$8MbMdEHGL3xb/XnebU3eTLeUyMqfRTzgPq8k1FHeFzE=', '2014-10-15 13:55:25', '1', 'test', '', '', 'test@test.com', '1', '1', '2014-10-15 13:55:25');
COMMIT;

-- ----------------------------
--  Table structure for `auth_user_groups`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `auth_user_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `django_admin_log`
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `django_content_type`
-- ----------------------------
BEGIN;
INSERT INTO `django_content_type` VALUES ('1', 'log entry', 'admin', 'logentry'), ('2', 'permission', 'auth', 'permission'), ('3', 'group', 'auth', 'group'), ('4', 'user', 'auth', 'user'), ('5', 'content type', 'contenttypes', 'contenttype'), ('6', 'session', 'sessions', 'session'), ('7', '市场', 'otc', 'region'), ('8', 'otc', 'otc', 'otc'), ('9', '市场容量', 'otc', 'industry'), ('10', '市场容量指数', 'otc', 'industry_index'), ('11', 'OTC公告', 'otc', 'otc_new'), ('12', 'OTC研告', 'otc', 'otc_study'), ('13', '近期热门证券', 'otc', 'otc_hot'), ('14', '基础数据', 'otc', 'otc_base');
COMMIT;

-- ----------------------------
--  Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `otc_industry`
-- ----------------------------
DROP TABLE IF EXISTS `otc_industry`;
CREATE TABLE `otc_industry` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `in_region_id` int(11) NOT NULL,
  `in_date` date NOT NULL,
  `in_num` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `otc_industry_44f77fb2` (`in_region_id`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `otc_industry`
-- ----------------------------
BEGIN;
INSERT INTO `otc_industry` VALUES ('1', '16', '2014-07-13', '23'), ('2', '1', '2014-07-13', '178'), ('3', '2', '2014-07-13', '205'), ('4', '3', '2014-07-13', '89'), ('5', '4', '2014-07-13', '48'), ('6', '5', '2014-07-13', '28'), ('7', '6', '2014-07-13', '16'), ('8', '7', '2014-07-13', '38'), ('9', '8', '2014-07-13', '19'), ('10', '9', '2014-07-13', '0'), ('11', '10', '2014-07-13', '47'), ('12', '11', '2014-07-14', '0'), ('13', '12', '2014-07-14', '188'), ('14', '13', '2014-07-14', '67'), ('15', '14', '2014-07-14', '11'), ('16', '15', '2014-07-14', '12'), ('17', '17', '2014-07-14', '34'), ('18', '18', '2014-07-18', '753');
COMMIT;

-- ----------------------------
--  Table structure for `otc_industry_index`
-- ----------------------------
DROP TABLE IF EXISTS `otc_industry_index`;
CREATE TABLE `otc_industry_index` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ii_date` date NOT NULL,
  `ii_index` decimal(15,5) NOT NULL,
  `ii_company` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=33 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `otc_otc`
-- ----------------------------
DROP TABLE IF EXISTS `otc_otc`;
CREATE TABLE `otc_otc` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `otc_region_id` int(11) NOT NULL,
  `otc_code` varchar(20) NOT NULL,
  `otc_name` varchar(100) NOT NULL,
  `otc_amount` decimal(15,5) NOT NULL,
  `otc_per` decimal(10,5) NOT NULL,
  `otc_amount_per` decimal(15,5) NOT NULL,
  `otc_days` int(11) NOT NULL,
  `otc_date` date NOT NULL,
  `otc_tot_amount` decimal(15,5) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `otc_otc_d8f65d2d` (`otc_region_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `otc_otc_base`
-- ----------------------------
DROP TABLE IF EXISTS `otc_otc_base`;
CREATE TABLE `otc_otc_base` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `base_date` date NOT NULL,
  `base_index` decimal(15,5) NOT NULL,
  `base_company_index` decimal(15,5) NOT NULL,
  `base_trans` decimal(15,5) NOT NULL,
  `base_company` int(15) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `otc_otc_base`
-- ----------------------------
BEGIN;
INSERT INTO `otc_otc_base` VALUES ('1', '2014-10-14', '208.22000', '269.74000', '251555.53000', '1756');
COMMIT;

-- ----------------------------
--  Table structure for `otc_otc_hot`
-- ----------------------------
DROP TABLE IF EXISTS `otc_otc_hot`;
CREATE TABLE `otc_otc_hot` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hot_sort` int(11) NOT NULL,
  `hot_company` varchar(30) NOT NULL,
  `hot_trans` decimal(15,5) NOT NULL,
  `hot_sum_trans` decimal(15,5) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `otc_otc_hot`
-- ----------------------------
BEGIN;
INSERT INTO `otc_otc_hot` VALUES ('1', '1', '上海安防', '3.50000', '30000.00000'), ('2', '2', '康捷宝', '6.71000', '2020000.00000'), ('3', '3', '康纶纤维', '7.15000', '3440000.00000'), ('4', '4', '宇度医学', '6.60000', '1420000.00000'), ('5', '5', '福升威尔', '7.60000', '100000.00000'), ('6', '6', '保罗生物', '7.72000', '5580000.00000'), ('7', '7', '钢软股份', '13.60000', '60000.00000'), ('8', '8', '吉天师', '6.73000', '1200000.00000'), ('9', '9', '悠游堂', '8.50000', '20000.00000'), ('10', '10', '电虎科技', '5.00000', '7480000.00000');
COMMIT;

-- ----------------------------
--  Table structure for `otc_otc_new`
-- ----------------------------
DROP TABLE IF EXISTS `otc_otc_new`;
CREATE TABLE `otc_otc_new` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `new_region_id` int(11) NOT NULL,
  `new_code` varchar(30) NOT NULL,
  `new_title` varchar(100) NOT NULL,
  `new_url` varchar(300) NOT NULL,
  `new_date` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `otc_otc_new_a9c70aa9` (`new_region_id`)
) ENGINE=MyISAM AUTO_INCREMENT=170 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `otc_otc_new`
-- ----------------------------
BEGIN;
INSERT INTO `otc_otc_new` VALUES ('1', '2', '100056_QL_EE', '火凤凰：公开转让说明书', 'http://file.chinascopefinancial.com/finrpts/file/2013Q4/2013Q4_QLEE_QL100056_FULL.pdf', '2014-07-12'), ('2', '2', '100056_QL_EE', ' 铂恩塞尔：审计报告', 'http://www.china-see.com/setc_admin/upload/myupload_5366.pdf', '2014-07-11'), ('3', '18', '100056_QL_EE', '康莱宝：全国中小企业股份转让系统有限责任公司关于', 'http://bjzr.gfzr.com.cn/fina/2014-07-11/64215446.PDF', '2014-07-11'), ('4', '18', '100056_QL_EE', '智信股份：全国中小企业股份转让系统有限责任公司', 'http://bjzr.gfzr.com.cn/fina/2014-07-11/64215449.PDF', '2014-07-11'), ('5', '18', '100056_QL_EE', '火凤凰：全国中小企业股份转让系统有限责任公司关于', 'http://bjzr.gfzr.com.cn/fina/2014-07-11/64215466.PDF', '2014-07-11'), ('6', '18', '100056_QL_EE', '关于全国中小企业股份转让系统网站调整的通知 ', 'http://bjzr.gfzr.com.cn/fina/2014-07-14/64209618.PDF', '2014-07-14'), ('7', '18', '100056_QL_EE', '优炫软件：变更持续督导主办券商公告 ', 'http://bjzr.gfzr.com.cn/fina/2014-07-14/64220037.PDF', '2014-07-13'), ('8', '18', '100056_QL_EE', '爱科凯能：2014年第二次临时股东大会决议公告 ', 'http://bjzr.gfzr.com.cn/fina/2014-07-14/64220086.PDF', '2014-07-14'), ('9', '18', '100056_QL_EE', '万人调查：对外投资的公告 ', 'http://bjzr.gfzr.com.cn/fina/2014-07-14/64220337.PDF', '2014-07-14'), ('10', '2', '100179', ' 惠云塑木：定向增资股份认购办法 ', 'http://bjzr.gfzr.com.cn/fina/2014-07-14/64220337.PDF', '2014-07-14'), ('11', '2', '100126', ' 鸿泰种业：2014年第一次临时股东大会决议公告', 'http://bjzr.gfzr.com.cn/fina/2014-07-14/64220337.PDF', '2014-07-14'), ('12', '2', '100126', ' 鸿泰种业：2014第一次临时股东大会的法律意见', 'http://bjzr.gfzr.com.cn/fina/2014-07-14/64220337.PDF', '2014-07-14'), ('13', '2', '100205 ', ' 志成农业：第一届监事会第四次会议决议公告', 'http://bjzr.gfzr.com.cn/fina/2014-07-14/64220337.PDF', '2014-07-14'), ('14', '2', '100053', ' 通化百泉：关于公司董事康岩增持公司股份限售的公告', 'http://bjzr.gfzr.com.cn/fina/2014-07-14/64220337.PDF', '2014-07-14'), ('15', '2', '100065', ' 盛泉养老：第一届董事会第九次会议决议公告 ', 'http://bjzr.gfzr.com.cn/fina/2014-07-14/64220337.PDF', '2014-07-14'), ('16', '2', '100030', ' 康岱生物：关于延期召开2013年年度股东大会的公告', 'http://bjzr.gfzr.com.cn/fina/2014-07-14/64220337.PDF', '2014-07-14'), ('17', '2', '100009 ', '保罗生物：重大事项暂停股份转让进展公告 ', 'http://bjzr.gfzr.com.cn/fina/2014-07-14/64220337.PDF', '2014-07-14'), ('18', '2', '100139 ', '光世农业：2014年第三次临时股东大会决议公告 ', 'http://bjzr.gfzr.com.cn/fina/2014-07-14/64220337.PDF', '2014-07-14'), ('19', '2', '100025 ', '易通股份：股份解除转让限制公告 ', 'http://bjzr.gfzr.com.cn/fina/2014-07-14/64220337.PDF', '2014-07-14'), ('20', '2', '100109 ', '佰康股份：定向增资方案 ', 'http://bjzr.gfzr.com.cn/fina/2014-07-14/64220337.PDF', '2014-07-14'), ('21', '2', '100095 ', '金匙环保：2013年年度股东大会决议公告 ', 'http://bjzr.gfzr.com.cn/fina/2014-07-14/64220337.PDF', '2014-07-14'), ('22', '3', '10689', '关于授予上海上会会计师事务所有限公司等25家机构专业服务商会员资格的通告', 'http://bjzr.gfzr.com.cn/fina/2014-07-14/64220337.PDF', '2014-07-14'), ('23', '3', '10688', '关于授予中信证券股份有限公司等66家机构推荐商会员资格的通告', 'http://bjzr.gfzr.com.cn/fina/2014-07-14/64220337.PDF', '2014-07-14'), ('24', '3', '10677', '关于授予中国工商银行股份有限公司浙江省分行等14家机构战略会员资格的通告', 'http://bjzr.gfzr.com.cn/fina/2014-07-14/64220337.PDF', '2014-07-14'), ('25', '3', '10778', '关于授予中国民生银行股份有限公司杭州分行战略会员资格的通告', 'http://bjzr.gfzr.com.cn/fina/2014-07-14/64220337.PDF', '2014-07-14'), ('26', '3', '10233', '关于授予杭州钱王会计师事务所等 11家机构专业服务商会员资格的通告', 'http://bjzr.gfzr.com.cn/fina/2014-07-14/64220337.PDF', '2014-07-14'), ('27', '3', '10456', '关于授予杭州鲲鹏投资管理有限公司等2家机构推荐商会员资格的通告', 'http://bjzr.gfzr.com.cn/fina/2014-07-14/64220337.PDF', '2014-07-14'), ('28', '3', '10888', '关于授予国富浩华会计师事务所等14家机构专业服务商会员资格的通告', 'http://bjzr.gfzr.com.cn/fina/2014-07-14/64220337.PDF', '2014-07-14'), ('29', '18', '831127', '[定期报告]祺龙股份：更正公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470204.PDF', '2014-10-14'), ('30', '18', '831127', '[定期报告]祺龙股份：2014年半年度报告（更新后）', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470205.PDF', '2014-10-14'), ('31', '18', '430434', '[临时公告]万泉河：股票解除限售公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470556.PDF', '2014-10-14'), ('32', '18', '430209', '[临时公告]康孚科技：第一届董事会第十二次会议决议公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470555.PDF', '2014-10-14'), ('33', '18', '430534', '[临时公告]天涌科技：股票发行认购公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470411.PDF', '2014-10-14'), ('34', '18', '831126', '[临时公告]元鼎科技：2014年第四次临时股东大会决议公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470410.PDF', '2014-10-14'), ('35', '18', '430140', '[临时公告]新眼光：定向发行情况报告书', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470609.PDF', '2014-10-14'), ('36', '18', '430140', '[临时公告]新眼光：北京大成（上海）律师事务所关于公司定向发行股份的法律意见书', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470408.PDF', '2014-10-14'), ('37', '18', '430140', '[临时公告]新眼光：关于公司定向发行股票将在全国股份转让系统挂牌公开转让的公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470409.PDF', '2014-10-14'), ('38', '18', '831190', '[临时公告]第六元素：关于公司股票将在全国股份转让系统挂牌公开转让的提示性公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470234.PDF', '2014-10-14'), ('39', '18', '831197', '[临时公告]雅洁源：关于公司股票将在全国股份转让系统挂牌公开转让的提示性公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470235.PDF', '2014-10-14'), ('40', '18', '831114', '[临时公告]易销科技：股票解除限售公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64468432.PDF', '2014-10-14'), ('41', '2', '100095', '金匙环保：2014年第三次临时股东大会决议公告', 'http://www.china-see.com/setc_admin/upload/myupload_6673.pdf', '2014-10-14'), ('42', '2', '100095', '金匙环保：2014年第三次临时股东大会的法律意见书', 'http://www.china-see.com/setc_admin/upload/myupload_6674.pdf', '2014-10-14'), ('43', '2', '100058', '泰锋刀具：第一届董事会第六次会议决议公告', 'http://www.china-see.com/setc_admin/upload/myupload_6668.pdf', '2014-10-14'), ('44', '2', '100139', '光世农业：关于公司完成工商变更登记的公告', 'http://www.china-see.com/setc_admin/upload/myupload_6669.pdf', '2014-10-14'), ('45', '2', '100068', '乔孚股份：2014年第三次临时股东大会决议公告', 'http://www.china-see.com/setc_admin/upload/myupload_6666.pdf', '2014-10-14'), ('46', '2', '100068', '乔孚股份：关于公司完成工商变更登记的公告', 'http://www.china-see.com/setc_admin/upload/myupload_6667.pdf', '2014-10-14'), ('47', '2', '100068', '乔孚股份：2014年第三次临时股东大会法律意见书', 'http://www.china-see.com/setc_admin/upload/myupload_6670.pdf', '2014-10-14'), ('48', '2', '100003', '康捷保：2014年第一次临时股东大会法律意见书', 'http://www.china-see.com/setc_admin/upload/myupload_6663.pdf', '2014-10-14'), ('49', '2', '100162', '慧升智能：关于公司完成工商变更登记的公告', 'http://www.china-see.com/setc_admin/upload/myupload_6678.pdf', '2014-10-14'), ('50', '2', '100185', '美瀚科技：2014年第一次临时股东大会决议公告', 'http://www.china-see.com/setc_admin/upload/myupload_6671.pdf', '2014-10-14'), ('51', '2', '100202', '建为历保：2014年第二次临时股东大会决议公告', 'http://www.china-see.com/setc_admin/upload/myupload_6643.pdf', '2014-10-14'), ('52', '2', '100202', '建为历保：2014年第二次临时股东大会法律意见书', 'http://www.china-see.com/setc_admin/upload/myupload_6644.pdf', '2014-10-14'), ('53', '2', '100003', '康捷保：2014年第一次临时股东大会决议公告', 'http://www.china-see.com/setc_admin/upload/myupload_6649.pdf', '2014-10-14'), ('54', '2', '100003', '康捷保：股份解除转让限制公告', 'http://www.china-see.com/setc_admin/upload/myupload_6661.pdf', '2014-10-14'), ('55', '2', '100162', '慧升智能：第一届董事会第七次会议决议公告暨召开2014年...', 'http://www.china-see.com/setc_admin/upload/myupload_6651.pdf', '2014-10-14'), ('56', '2', '100278', '康丽股份：法律意见书', 'http://www.china-see.com/setc_admin/upload/myupload_6657.pdf', '2014-10-13'), ('57', '2', '100278', '康丽股份：公司章程', 'http://www.china-see.com/setc_admin/upload/myupload_6658.pdf', '2014-10-13'), ('58', '2', '100278', '康丽股份：审计报告', 'http://www.china-see.com/setc_admin/upload/myupload_6659.pdf', '2014-10-13'), ('59', '2', '100278', '康丽股份：股份转让说明书', 'http://www.china-see.com/setc_admin/upload/myupload_6660.pdf', '2014-10-13'), ('60', '12', '', '河北万盛美纸业股份有限公司2014年度中期报告', 'http://www.tjsoc.com/web/pdf/信息披露/河北万盛美纸业股份有限公司2014年度中期报告.pdf', '2014-10-13'), ('61', '12', '', '湖北纽斯达食品股份有限公司2014年度中期报告', 'http://www.tjsoc.com/web/pdf/信息披露/湖北纽斯达食品股份有限公司2014年度中期报告.pdf', '2014-10-13'), ('62', '12', '', '广西桂林天然食品股份有限公司2014年中期报告', 'http://www.tjsoc.com/web/pdf/信息披露/广西桂林天然食品股份有限公司2014年度中期报告.pdf', '2014-10-13'), ('63', '12', '', '东营海丰石油化工股份有限公司关于召开2014年第一次临时股东大会的通知', 'http://www.tjsoc.com/web/pdf/信息披露/东营海丰石油化工股份有限公司关于召开2014年第一次临时股东大会的通知.pdf', '2014-10-13'), ('64', '12', '', '东营海丰石油化工股份有限公司第一届董事会2014年第二次会议决议公告', 'http://www.tjsoc.com/web/pdf/信息披露/东营海丰石油化工股份有限公司第一届董事会2014年第二次会议决议公告.pdf', '2014-10-13'), ('65', '12', '', '湖北茂弘纺织股份有限公司关于生产经营状况的重大事项公告', 'http://www.tjsoc.com/web/pdf/信息披露/湖北茂弘纺织股份有限公司关于生产经营状况的重大事项公告（201410.13）.pdf', '2014-10-13'), ('66', '12', '', '广东广济堂医药实业股份有限公司关于延长停牌时间的公告', 'http://www.tjsoc.com/web/pdf/信息披露/广东广济堂医药实业股份有限公司关于延长停牌时间的公告(2014.10.13).pdf', '2014-10-13'), ('67', '12', '', '湖南飘峰电气股份有限公司关于延期披露2014年中期报告并停牌的公告', 'http://www.tjsoc.com/web/pdf/信息披露/湖南飘峰电气股份有限公司关于延期披露2014年中期报告并停牌的公告.pdf', '2014-10-13'), ('68', '12', '', '河北鲁梅卡机械制造股份有限公司2014年第三季度重大事项声明', 'http://www.tjsoc.com/web/pdf/信息披露/河北鲁梅卡机械制造股份有限公司2014年第三季度重大事项声明.pdf', '2014-10-13'), ('69', '12', '', '沧州中天伟业商城股份有限公司2014年第三季度重大事项声明', 'http://www.tjsoc.com/web/pdf/信息披露/沧州中天伟业商城股份有限公司2014年第三季度重大事项声明.pdf', '2014-10-13'), ('70', '12', '', '沧兴集团商砼股份有限公司2014年第三季度重大事项声明', 'http://www.tjsoc.com/web/pdf/信息披露/沧兴集团商砼股份有限公司2014年第三季度重大事项声明.pdf', '2014-10-13'), ('71', '12', '', '吉林远通路桥工程集团股份有限公司2014年第三季度重大事项声明', 'http://www.tjsoc.com/web/pdf/信息披露/吉林远通路桥工程股份有限公司2014年第三季度重大事项声明.pdf', '2014-10-13'), ('72', '12', '', '巴中市天豪生态农业综合开发股份有限公司2014年第三季度重大事项声明', 'http://www.tjsoc.com/web/pdf/信息披露/巴中市天豪生态农业综合开发股份有限公司2014年第三季度重大事项声明.pdf', '2014-10-13'), ('73', '12', '', '石家庄清凉湾热力股份有限公司关于完成重组过程中评估报告的说明', 'http://www.tjsoc.com/web/pdf/信息披露/石家庄清凉湾热力股份有限公司关于完成重组过程中评估报告的说明.pdf', '2014-10-13'), ('74', '12', '', '四川御营春酒业股份有限公司关于公司抵押借款的重大事项公告', 'http://www.tjsoc.com/web/pdf/信息披露/四川御营春酒业股份有限公司关于公司抵押借款的重大事项公告（2014.10.13）.pdf', '2014-10-13'), ('75', '12', '', '四川御营春酒业股份有限公司第一届董事会2014年第五次会议决议公告', 'http://www.tjsoc.com/web/pdf/信息披露/四川御营春酒业股份有限公司第一届董事会2014年第五次会议决议公告.pdf', '2014-10-13'), ('76', '12', '', '甘肃巨鹏食品股份有限公司停牌公告', 'http://www.tjsoc.com/web/pdf/信息披露/甘肃巨鹏食品股份有限公司停牌公告(2014.10.11).pdf', '2014-10-11'), ('77', '12', '', '甘肃巨鹏食品股份有限公司关于召开2014年第二次临时股东大会的通知', 'http://www.tjsoc.com/web/pdf/信息披露/甘肃巨鹏食品股份有限公司关于召开2014年第二次临时股东大会的通知.pdf', '2014-10-11'), ('78', '12', '', '甘肃巨鹏食品股份有限公司第一届董事会第四次会议决议的公告', 'http://www.tjsoc.com/web/pdf/信息披露/甘肃巨鹏食品股份有限公司第一届董事会第四次会议决议的公告.pdf', '2014-10-11'), ('79', '12', '', '黑龙江鹿源春鹿业股份有限公司关于董事变更的公告', 'http://www.tjsoc.com/web/pdf/信息披露/黑龙江鹿源春鹿业股份有限公司关于董事变更的公告(2014.10.11).pdf', '2014-10-11'), ('80', '18', '830902', '[临时公告]长仪股份：2014年第二次临时股东大会决议公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470756.PDF', '2014-10-14'), ('81', '18', '830902', '[临时公告]长仪股份：股票发行认购公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470757.PDF', '2014-10-14'), ('82', '18', '831082', '[临时公告]汇鑫嘉德：2014年第六次临时股东大会决议公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470745.PDF', '2014-10-14'), ('83', '18', '430035', '[临时公告]中 兴 通：关于2014年半年度权益分派实施的更正公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470746.PDF', '2014-10-14'), ('84', '18', '831118', '[临时公告]兰亭科技：2014年第三次临时股东大会会议决议公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470744.PDF', '2014-10-14'), ('85', '18', '430371', '[临时公告]科传股份：关于子公司收购股权的公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470669.PDF', '2014-10-14'), ('86', '18', '430371', '[临时公告]科传股份：第二届董事会第十一次会议决议公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470670.PDF', '2014-10-14'), ('87', '18', '430758', '[临时公告]四联智能：对外担保公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470643.PDF', '2014-10-14'), ('88', '18', '430758', '[临时公告]四联智能：第六届董事会第四次会议决议公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470644.PDF', '2014-10-14'), ('89', '18', '830782', '[临时公告]泰安众诚：更正公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470641.PDF', '2014-10-14'), ('90', '18', '830782', '[临时公告]泰安众诚：股票发行方案（更新后）', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470642.PDF', '2014-10-14'), ('91', '18', '430413', '[临时公告]沄辉科技：2014年第一次临时股东会议决议公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470637.PDF', '2014-10-14'), ('92', '18', '430413', '[临时公告]沄辉科技：股份发行认购公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470638.PDF', '2014-10-14'), ('93', '18', '430675', '[临时公告]天跃科技：2014年第三次临时股东大会决议公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470632.PDF', '2014-10-14'), ('94', '18', '430675', '[临时公告]天跃科技：关于公司2014年第三次临时股东大会法律意见书', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470633.PDF', '2014-10-14'), ('95', '18', '430675', '[临时公告]天跃科技：股票发行认购公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470634.PDF', '2014-10-14'), ('96', '18', '430140', '[券商公告]新眼光：中信建投证券股份有限公司关于公司股票发行合法合规性的专项意见', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470407.PDF', '2014-10-14'), ('97', '18', '831219', '[临时公告]詹氏食品：公开转让说明书', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471118.PDF', '2014-10-14'), ('98', '18', '831219', '[临时公告]詹氏食品：公司章程', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471124.PDF', '2014-10-14'), ('99', '18', '831219', '[临时公告]詹氏食品：审计报告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471119.PDF', '2014-10-14'), ('100', '18', '831219', '[临时公告]詹氏食品：关于公司股票申请进入全国中小企业股份转让系统挂牌转让之补充法律意见书', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471121.PDF', '2014-10-14'), ('101', '18', '831219', '[临时公告]詹氏食品：关于公司股票申请进入全国中小企业股份转让系统挂牌转让之补充法律意见书（二）', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471122.PDF', '2014-10-14'), ('102', '18', '831219', '[临时公告]詹氏食品：关于公司股票申请进入全国中小企业股份转让系统挂牌转让之补充法律意见书（三）', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471123.PDF', '2014-10-14'), ('103', '18', '831219', '[临时公告]詹氏食品：关于公司股票申请进入全国中小企业股份转让系统挂牌转让之法律意见书', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471120.PDF', '2014-10-14'), ('104', '18', '831219', '[券商公告]詹氏食品：国元证券股份有限公司关于推荐公司股票进入全国中小企业股份转让系统挂牌转让的推荐报告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471125.PDF', '2014-10-14'), ('105', '18', '831219', '[业务通知]詹氏食品：全国中小企业股份转让系统有限责任公司关于同意公司股票在全国中小企业股份转让系统挂牌的函', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471126.PDF', '2014-10-14'), ('106', '18', '831212', '[临时公告]耐磨科技：公开转让说明书', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471128.PDF', '2014-10-14'), ('107', '18', '831212', '[临时公告]耐磨科技：公司章程', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471131.PDF', '2014-10-14'), ('108', '18', '831212', '[临时公告]耐磨科技：审计报告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471132.PDF', '2014-10-14'), ('109', '18', '831212', '[临时公告]耐磨科技：北京德恒（昆明）律师事务所关于公司申请股票在全国中小企业股份转让系统挂牌并公开转让的补充法律意见书', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471134.PDF', '2014-10-14'), ('110', '18', '831212', '[临时公告]耐磨科技：北京德恒（昆明）律师事务所关于公司申请股票在全国中小企业股份转让系统挂牌并公开转让的法律意见书', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471133.PDF', '2014-10-14'), ('111', '18', '831212', '[券商公告]耐磨科技：太平洋证券股份有限公司关于推荐公司股票在全国中小企业股份转让系统挂牌的推荐报告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471127.PDF', '2014-10-14'), ('112', '18', '831212', '[业务通知]耐磨科技：全国中小企业股份转让系统有限责任公司关于同意公司股票在全国中小企业股份转让系统挂牌的函', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471135.PDF', '2014-10-14'), ('113', '18', '430088', '[临时公告]七维航测：第二届董事会第八次会议决议公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471454.PDF', '2014-10-14'), ('114', '18', '430088', '[临时公告]七维航测：关于召开2014年第五次临时股东大会通知的公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471455.PDF', '2014-10-14'), ('115', '18', '430088', '[临时公告]七维航测：股票发行方案', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471458.PDF', '2014-10-14'), ('116', '18', '831073', '[临时公告]瑞恒科技：第一届董事会第四次会议决议公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471453.PDF', '2014-10-14'), ('117', '18', '430724', '[临时公告]芳笛环保：召开2014年第五次临时股东大会的通知', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471440.PDF', '2014-10-14'), ('118', '18', '430724', '[临时公告]芳笛环保：第一届董事会第十次会议决议公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471441.PDF', '2014-10-14'), ('119', '18', '430724', '[临时公告]芳笛环保：关于2013年利润分配预案的公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471442.PDF', '2014-10-14'), ('120', '18', '430220', '[临时公告]迈达科技：关于召开2014年第一次临时股东大会通知公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471438.PDF', '2014-10-14'), ('121', '18', '430220', '[临时公告]迈达科技：第一届董事会第九次会议决议公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471439.PDF', '2014-10-14'), ('122', '18', '831186', '[临时公告]金鸿药业：第一届董事会第九次会议决议公告暨召开2014年第二次临时股东大会的通知', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471436.PDF', '2014-10-14'), ('123', '18', '831186', '[临时公告]金鸿药业：第一届监事会第七次会议决议公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471437.PDF', '2014-10-14'), ('124', '18', '430393', '[临时公告]三景科技：关于会计估计变更的公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471431.PDF', '2014-10-14'), ('125', '18', '430393', '[临时公告]三景科技：第一届董事会第十一次会议决议公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471432.PDF', '2014-10-14'), ('126', '18', '430393', '[临时公告]三景科技：第一届监事会第六次会议决议公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471433.PDF', '2014-10-14'), ('127', '18', '430035', '[临时公告]中 兴 通：2014年半年度权益分派实施公告（更新后）', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471425.PDF', '2014-10-14'), ('128', '18', '430014', '[临时公告]恒业世纪：关于辽宁深港投资有限公司资金往来情况的说明公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471424.PDF', '2014-10-14'), ('129', '18', '430147', '[临时公告]中矿龙科：2014年第二次临时股东大会决议公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471426.PDF', '2014-10-14'), ('130', '18', '831029', '[临时公告]银丰棉花：第四届董事会第六次会议决议公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471422.PDF', '2014-10-14'), ('131', '18', '831029', '[临时公告]银丰棉花：出售资产的公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471423.PDF', '2014-10-14'), ('132', '18', '430518', '[临时公告]嘉达早教：股票发行认购公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471419.PDF', '2014-10-14'), ('133', '18', '430518', '[临时公告]嘉达早教：2014年第三次临时股东大会的法律意见书', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471420.PDF', '2014-10-14'), ('134', '18', '430518', '[临时公告]嘉达早教：2014年第三次临时股东大会决议公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471421.PDF', '2014-10-14'), ('135', '18', '430762', '[临时公告]荣昌育种：2014年第六次临时股东大会决议公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471184.PDF', '2014-10-14'), ('136', '18', '430711', '[临时公告]泓源光电：第一届监事会第五次会议决议公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471180.PDF', '2014-10-14'), ('137', '18', '430711', '[临时公告]泓源光电：关于监事变更公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471181.PDF', '2014-10-14'), ('138', '18', '430711', '[临时公告]泓源光电：2014年第一次临时股东大会的见证意见', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471182.PDF', '2014-10-14'), ('139', '18', '430711', '[临时公告]泓源光电：2014年第一次临时股东大会决议公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471183.PDF', '2014-10-14'), ('140', '18', '831068', '[临时公告]凌志环保：关于子公司沭阳凌志水务有限公司与江苏省沭阳县人民政府签订《关于沭阳经济开发区8万立方米/日工业污水处理厂项目特许经营权协议》之补充合同的公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471168.PDF', '2014-10-14'), ('141', '18', '831068', '[临时公告]凌志环保：2014年第三次临时股东大会决议公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471169.PDF', '2014-10-14'), ('142', '18', '430297', '[临时公告]金硕信息：关于董监高变动的公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471162.PDF', '2014-10-14'), ('143', '18', '430604', '[临时公告]三炬生物：首批股票解除限售公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471163.PDF', '2014-10-14'), ('144', '18', '430673', '[临时公告]天佑铁道：关于获得北车集团城轨车轮消音环订单的公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471164.PDF', '2014-10-14'), ('145', '18', '430238', '[临时公告]普华科技：关于完成工商变更登记的公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471028.PDF', '2014-10-14'), ('146', '18', '430416', '[临时公告]地林伟业：股票解除限售公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471029.PDF', '2014-10-14'), ('147', '18', '430707', '[临时公告]欧神诺：2014年第三次临时股东大会决议公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471032.PDF', '2014-10-14'), ('148', '18', '430301', '[临时公告]倚天股份：第一届董事会第十一次会议决议公告暨召开2014年第二次临时股东大会的通知', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64471070.PDF', '2014-10-14'), ('149', '18', '430033', '[临时公告]彩讯科技：关于财务总监、董事会秘书辞职公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470848.PDF', '2014-10-14'), ('150', '18', '830808', '[临时公告]中智华体：关于选举职工代表监事的公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470844.PDF', '2014-10-14'), ('151', '18', '830808', '[临时公告]中智华体：关于第一届董事会第四次会议决议暨召开2014年第一次临时股东大会的公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470845.PDF', '2014-10-14'), ('152', '18', '830808', '[临时公告]中智华体：关于第一届监事会第三次会议决议公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470846.PDF', '2014-10-14'), ('153', '18', '430594', '[临时公告]盈光科技：关于公司2014年第三次临时股东大会的法律意见书', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470839.PDF', '2014-10-14'), ('154', '18', '430594', '[临时公告]盈光科技：2014年第三次临时股东大会决议公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470840.PDF', '2014-10-14'), ('155', '18', '430594', '[临时公告]盈光科技：关于公司关联方为子公司开平市盈光机电科技有限公司融资租赁业务提供担保的关联交易公告', 'http://bjzr.gfzr.com.cn/fina/2014-10-14/64470841.PDF', '2014-10-14'), ('156', '2', '100198', '磊诺安防：2014年第三次临时股东大会法律意见书', 'http://www.china-see.com/setc_admin/upload/myupload_6682.pdf', '2014-10-14'), ('157', '2', '100280', '联诚科技：法律意见书', 'http://www.china-see.com/setc_admin/upload/myupload_6695.pdf', '2014-10-14'), ('158', '2', '100280', '联诚科技：审计报告', 'http://www.china-see.com/setc_admin/upload/myupload_6694.pdf', '2014-10-14'), ('159', '2', '100280', '联诚科技：公司章程', 'http://www.china-see.com/setc_admin/upload/myupload_6693.pdf', '2014-10-14'), ('160', '2', '100280', '联诚科技：股份转让说明书', 'http://www.china-see.com/setc_admin/upload/myupload_6692.pdf', '2014-10-14'), ('161', '2', '100192', '国富光启：2014年第一次临时股东大会决议公告', 'http://www.china-see.com/setc_admin/upload/myupload_6687.pdf', '2014-10-14'), ('162', '2', '100192', '国富光启：2014年第一次临时股东大会法律意见书', 'http://www.china-see.com/setc_admin/upload/myupload_6688.pdf', '2014-10-14'), ('163', '2', '100205', '志成农业：2014年第四次临时股东大会决议公告', 'http://www.china-see.com/setc_admin/upload/myupload_6685.pdf', '2014-10-14'), ('164', '2', '100205', '志成农业：2014年第四次临时股东大会法律意见书', 'http://www.china-see.com/setc_admin/upload/myupload_6686.pdf', '2014-10-14'), ('165', '2', '100256', '桃花源：2014年第二次临时股东大会的法律意见书', 'http://www.china-see.com/setc_admin/upload/myupload_6697.pdf', '2014-10-14'), ('166', '2', '100256', '桃花源：2014年第二次临时股东大会决议的公告', 'http://www.china-see.com/setc_admin/upload/myupload_6696.pdf', '2014-10-14'), ('167', '2', '100185', '美瀚科技：2014年第一次临时股东大会的法律意见书', 'http://www.china-see.com/setc_admin/upload/myupload_6672.pdf', '2014-10-13'), ('168', '12', '', '宁夏白浪包装股份有限公司关于获得“2014年宁夏回族自治区专精特新中小企业”的公告', 'http://www.tjsoc.com/web/pdf/信息披露/宁夏白浪包装股份有限公司关于获得“2014年宁夏回族自治区专精特新中小企业”的公告.pdf', '2014-10-14'), ('169', '12', '', '山东博特精工股份有限公司第三届董事会第三次会议决议公告', 'http://www.tjsoc.com/web/pdf/信息披露/山东博特精工股份有限公司第三届董事会第三次会议决议公告.pdf', '2014-10-14');
COMMIT;

-- ----------------------------
--  Table structure for `otc_otc_study`
-- ----------------------------
DROP TABLE IF EXISTS `otc_otc_study`;
CREATE TABLE `otc_otc_study` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stu_code` varchar(30) NOT NULL,
  `stu_title` varchar(100) NOT NULL,
  `stu_url` varchar(100) NOT NULL,
  `stu_date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `otc_otc_study`
-- ----------------------------
BEGIN;
INSERT INTO `otc_otc_study` VALUES ('1', '1', '2014年5月场外市场报告', 'pdf/2014年5月场外市场报告.pdf', '2014-07-14'), ('2', '2', '2014年4月场外市场报告', 'pdf/2014年4月场外市场报告.pdf', '2014-07-14'), ('3', '3', '2014年3月场外市场报告', 'pdf/2014年3月场外市场报告.pdf', '2014-07-14'), ('4', '4', '2014年2月场外市场报告', 'pdf/2014年2月场外市场报告.pdf', '2014-07-14'), ('5', '5', '资本市场改革与扩容打开创投成长空间', 'pdf/资本市场改革与扩容打开创投成长空间_3.pdf', '2014-07-14'), ('6', '6', '申银万国-新三板挂牌公司2013年年报分析', 'pdf/申银万国-新三板挂牌公司2013年年报分析_1.pdf', '2014-07-14'), ('7', '7', '行业研究：激活新三板市场交易，提升流动性', 'pdf/华泰证券-行业研究激活新三板市场交易提升流动性.pdf', '2014-07-14'), ('8', '8', '2013年上海自贸区与深圳前海发展研究报告', 'pdf/2013年上海自贸区与深圳前海发展研究报告简版.pdf', '2014-07-14'), ('9', '9', '818家新三板企业深度梳理', 'pdf/818家新三板企业深度梳理_.pdf', '2014-07-08');
COMMIT;

-- ----------------------------
--  Table structure for `otc_region`
-- ----------------------------
DROP TABLE IF EXISTS `otc_region`;
CREATE TABLE `otc_region` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `reg_name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `otc_region`
-- ----------------------------
BEGIN;
INSERT INTO `otc_region` VALUES ('1', '齐鲁'), ('2', '上海'), ('3', '浙江'), ('4', '武汉'), ('5', '辽宁'), ('6', '山西'), ('7', '海峡'), ('8', '广州'), ('9', '前海'), ('10', '新疆'), ('11', '北京'), ('12', '天津'), ('13', '重庆'), ('14', '吉林'), ('15', '甘肃'), ('16', '江苏'), ('17', '安徽'), ('18', '中小股转');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
