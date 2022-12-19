-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306:3306
-- Generation Time: Dec 19, 2022 at 11:06 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `automation`
--

-- --------------------------------------------------------

--
-- Table structure for table `audit_trails`
--

CREATE TABLE `audit_trails` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `user_id` int(11) NOT NULL,
  `event` varchar(255) NOT NULL,
  `module` varchar(255) NOT NULL,
  `data` text NOT NULL,
  `url` text NOT NULL,
  `ip` varchar(255) NOT NULL,
  `agent` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `audit_trails`
--

INSERT INTO `audit_trails` (`id`, `user_id`, `event`, `module`, `data`, `url`, `ip`, `agent`, `created_at`, `updated_at`) VALUES
(1, 1, 'Edit', ' Systemsetting', '{\"system_name\":\"Systemname\",\"editid\":\"1\",\"website_keywords\":\"[{\\\"value\\\":\\\"abc\\\"}]\",\"author\":\"metronic\",\"date_formate\":\"1\",\"decimal_point\":\"2\",\"footer_text\":\"metronic\",\"footer_link\":\"metronic\",\"website_description\":\"metronic\",\"website_logo\":null,\"website_logo_remove\":null,\"favicon_icon\":null,\"website_favicon_remove\":null,\"theme_color\":\"#f4911e\",\"sidebar_color\":\"#ffffff\",\"sidebar_active_menu_color\":\"#e51937\",\"sidebar_menu_color\":\"#000000\",\"sidebar_navbar_background_color\":\"#ffffff\",\"sidebar_navbar_font_color\":\"#000000\",\"header_navbar_background_color\":\"#ffffff\",\"header_navbar_font_color\":\"#000000\"}', 'admin/save-system-setting', '::1', 'Chrome', '2022-11-23 15:26:08', '2022-11-23 15:26:08'),
(2, 1, 'Edit', ' Systemsetting', '{\"system_name\":\"Systemname\",\"editid\":\"1\",\"website_keywords\":\"[{\\\"value\\\":\\\"abc\\\"}]\",\"author\":\"metronic\",\"date_formate\":\"1\",\"decimal_point\":\"2\",\"footer_text\":\"metronic\",\"footer_link\":\"metronic\",\"website_description\":\"metronic\",\"website_logo\":null,\"website_logo_remove\":null,\"favicon_icon\":null,\"website_favicon_remove\":null,\"theme_color\":\"#f4911e\",\"sidebar_color\":\"#ffffff\",\"sidebar_active_menu_color\":\"#e51937\",\"sidebar_menu_color\":\"#f4911e\",\"sidebar_navbar_background_color\":\"#ffffff\",\"sidebar_navbar_font_color\":\"#f4911e\",\"header_navbar_background_color\":\"#ffffff\",\"header_navbar_font_color\":\"#000000\"}', 'admin/save-system-setting', '::1', 'Chrome', '2022-11-23 15:26:58', '2022-11-23 15:26:58'),
(3, 1, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Facebook\"],\"url\":[\"https:\\/\\/www.facebook.com\"],\"country_code\":[\"91\"],\"generateotp\":[\"N\"],\"mobile_number\":[\"9428776203\"]}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-11-23 15:38:30', '2022-11-23 15:38:30'),
(4, 1, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Whatsapp\"],\"url\":[null],\"country_code\":[\"91\"],\"generateotp\":[\"N\"],\"mobile_number\":[\"9428776203\"]}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-11-23 15:39:13', '2022-11-23 15:39:13'),
(5, 1, 'Edit', 'Brand Entry', '{\"brand_name\":\"Whatsapp\",\"editId\":\"2\",\"url\":\"-\",\"country_code\":\"91\",\"generateotp\":\"Y\",\"mobile_number\":\"9428776203\",\"generate_otp_switch\":\"yes\"}', 'admin/edit-save-brand-entry', '::1', 'Chrome', '2022-11-23 15:39:24', '2022-11-23 15:39:24'),
(6, 1, 'Edit', 'Brand Entry', '{\"brand_name\":\"Facebook\",\"editId\":\"1\",\"url\":\"https:\\/\\/www.facebook.com\",\"country_code\":\"91\",\"generateotp\":\"Y\",\"mobile_number\":\"9428776203\",\"generate_otp_switch\":\"yes\"}', 'admin/edit-save-brand-entry', '::1', 'Chrome', '2022-11-23 15:39:26', '2022-11-23 15:39:26'),
(7, 2, 'Update', 'Update Profile', '{\"first_name\":\"GRB\",\"edit_id\":\"2\",\"last_name\":\"Comviva\",\"email\":\"grb@comviva.com\",\"userimage\":\"userimage1669190261.jpg\"}', 'admin/admin-save-profile', '::1', 'Chrome', '2022-11-23 15:57:41', '2022-11-23 15:57:41'),
(8, 2, 'Update', 'Change Password', '{\"editid\":\"2\"}', 'admin/save-password', '::1', 'Chrome', '2022-11-23 15:58:35', '2022-11-23 15:58:35'),
(9, 2, 'Insert', 'Mobile Number', '{\"country_code\":\"101\",\"mobile_number\":\"9824345559\",\"operator\":\"jio\",\"status\":\"A\"}', 'admin/add-save-mobile-number', '::1', 'Chrome', '2022-11-28 19:48:10', '2022-11-28 19:48:10'),
(10, 2, 'Insert', 'Device', '{\"device_name\":\"samsung\",\"status\":\"A\"}', 'admin/add-save-device', '::1', 'Chrome', '2022-11-28 19:49:57', '2022-11-28 19:49:57'),
(11, 2, 'Edit', 'Brand Entry', '{\"brand_name\":\"Facebook\",\"editId\":\"1\",\"url\":\"https:\\/\\/www.facebook.com\",\"country_code\":\"91\",\"generateotp\":\"Y\",\"mobile_number\":\"9428776222\",\"generate_otp_switch\":\"yes\"}', 'admin/edit-save-brand-entry', '::1', 'Chrome', '2022-11-28 21:33:03', '2022-11-28 21:33:03'),
(12, 1, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Google\"],\"url\":[\"https:\\/\\/accounts.google.com\\/signin\\/v2\\/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin\"],\"country_code\":[\"91\"],\"generateotp\":[\"Y\"],\"mobile_number\":[\"9428776203\"],\"generate_otp_switch\":\"yes\"}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-11-29 16:20:42', '2022-11-29 16:20:42'),
(13, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Snapchat\"],\"url\":[\"-\"],\"country_code\":[\"91\"],\"generateotp\":[\"N\"],\"mobile_number\":[\"9909267779\"]}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 04:30:45', '2022-12-16 04:30:45'),
(14, 2, 'Edit', 'Brand Entry', '{\"brand_name\":\"Snapchat\",\"editId\":\"4\",\"url\":\"-\",\"country_code\":\"91\",\"generateotp\":\"Y\",\"mobile_number\":\"9909267779\",\"generate_otp_switch\":\"yes\"}', 'admin/edit-save-brand-entry', '::1', 'Chrome', '2022-12-16 04:31:03', '2022-12-16 04:31:03'),
(15, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Hopper\"],\"url\":[\"-\"],\"country_code\":[\"+91\"],\"generateotp\":[\"Y\"],\"mobile_number\":[\"9427489760\"],\"generate_otp_switch\":\"yes\"}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 04:34:25', '2022-12-16 04:34:25'),
(16, 2, 'Edit', 'Brand Entry', '{\"brand_name\":\"Hopper\",\"editId\":\"5\",\"url\":\"-\",\"country_code\":\"91\",\"generateotp\":\"Y\",\"mobile_number\":\"9427489760\",\"generate_otp_switch\":\"yes\"}', 'admin/edit-save-brand-entry', '::1', 'Chrome', '2022-12-16 04:34:45', '2022-12-16 04:34:45'),
(17, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Afyapap\"],\"url\":[\"-\"],\"country_code\":[\"91\"],\"generateotp\":[\"Y\"],\"mobile_number\":[\"9909268558\"],\"generate_otp_switch\":\"yes\"}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 04:47:55', '2022-12-16 04:47:55'),
(18, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Airbnb\"],\"url\":[\"-\"],\"country_code\":[\"91\"],\"generateotp\":[\"Y\"],\"mobile_number\":[\"9909258779\"],\"generate_otp_switch\":\"yes\"}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 04:48:39', '2022-12-16 04:48:39'),
(19, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Binance\"],\"url\":[\"-\"],\"country_code\":[\"91\"],\"generateotp\":[\"Y\"],\"mobile_number\":[\"9909268997\"],\"generate_otp_switch\":\"yes\"}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 04:50:05', '2022-12-16 04:50:05'),
(20, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Boomplay\"],\"url\":[\"-\"],\"country_code\":[\"91\"],\"generateotp\":[\"Y\"],\"mobile_number\":[\"9909268997\"],\"generate_otp_switch\":\"yes\"}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 04:51:00', '2022-12-16 04:51:00'),
(21, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Clubhouse\"],\"url\":[\"-\"],\"country_code\":[\"91\"],\"generateotp\":[\"Y\"],\"mobile_number\":[\"9909268997\"],\"generate_otp_switch\":\"yes\"}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 04:51:38', '2022-12-16 04:51:38'),
(22, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Ding\"],\"url\":[\"-\"],\"country_code\":[\"91\"],\"generateotp\":[\"Y\"],\"mobile_number\":[\"9909268997\"],\"generate_otp_switch\":\"yes\"}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 04:52:30', '2022-12-16 04:52:30'),
(23, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Imo\"],\"url\":[\"-\"],\"country_code\":[\"91\"],\"generateotp\":[\"Y\"],\"mobile_number\":[\"9909268997\"],\"generate_otp_switch\":\"yes\"}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 04:53:41', '2022-12-16 04:53:41'),
(24, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Instagram\"],\"url\":[\"-\"],\"country_code\":[\"91\"],\"generateotp\":[\"Y\"],\"mobile_number\":[\"9909268997\"],\"generate_otp_switch\":\"yes\"}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 04:54:11', '2022-12-16 04:54:11'),
(25, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Instagramlite\"],\"url\":[\"-\"],\"country_code\":[\"91\"],\"generateotp\":[\"Y\"],\"mobile_number\":[\"9909268997\"],\"generate_otp_switch\":\"yes\"}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 04:54:50', '2022-12-16 04:54:50'),
(26, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Letshego\"],\"url\":[\"-\"],\"country_code\":[\"91\"],\"generateotp\":[\"Y\"],\"mobile_number\":[\"9909268997\"],\"generate_otp_switch\":\"yes\"}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 04:55:25', '2022-12-16 04:55:25'),
(27, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Linkedin\"],\"url\":[\"-\"],\"country_code\":[\"91\"],\"generateotp\":[\"Y\"],\"mobile_number\":[\"9909268997\"],\"generate_otp_switch\":\"yes\"}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 04:55:55', '2022-12-16 04:55:55'),
(28, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Signal\"],\"url\":[\"-\"],\"country_code\":[\"91\"],\"generateotp\":[\"Y\"],\"mobile_number\":[\"9909268997\"],\"generate_otp_switch\":\"yes\"}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 04:56:28', '2022-12-16 04:56:28'),
(29, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Spotify\"],\"url\":[\"-\"],\"country_code\":[\"91\"],\"generateotp\":[\"Y\"],\"mobile_number\":[\"9909268997\"],\"generate_otp_switch\":\"yes\"}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 04:57:08', '2022-12-16 04:57:08'),
(30, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Telegram\"],\"url\":[\"-\"],\"country_code\":[\"91\"],\"generateotp\":[\"Y\"],\"mobile_number\":[\"9909268997\"],\"generate_otp_switch\":\"yes\"}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 04:57:35', '2022-12-16 04:57:35'),
(31, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Tinder\"],\"url\":[\"-\"],\"country_code\":[\"91\"],\"generateotp\":[\"Y\"],\"mobile_number\":[\"9909268997\"],\"generate_otp_switch\":\"yes\"}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 04:58:09', '2022-12-16 04:58:09'),
(32, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Truecaller\"],\"url\":[\"-\"],\"country_code\":[\"91\"],\"generateotp\":[\"Y\"],\"mobile_number\":[\"9909268997\"],\"generate_otp_switch\":\"yes\"}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 04:58:48', '2022-12-16 04:58:48'),
(33, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Twitter\"],\"url\":[\"-\"],\"country_code\":[\"91\"],\"generateotp\":[\"Y\"],\"mobile_number\":[\"9909268997\"],\"generate_otp_switch\":\"yes\"}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 04:59:18', '2022-12-16 04:59:18'),
(34, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Uber\"],\"url\":[\"-\"],\"country_code\":[\"91\"],\"generateotp\":[\"Y\"],\"mobile_number\":[\"9909268997\"],\"generate_otp_switch\":\"yes\"}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 04:59:53', '2022-12-16 04:59:53'),
(35, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Viber\"],\"url\":[\"-\"],\"country_code\":[\"91\"],\"generateotp\":[\"Y\"],\"mobile_number\":[\"9909268997\"],\"generate_otp_switch\":\"yes\"}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 05:00:25', '2022-12-16 05:00:25'),
(36, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"VKMusic\"],\"url\":[\"-\"],\"country_code\":[\"91\"],\"generateotp\":[\"Y\"],\"mobile_number\":[\"9909268997\"],\"generate_otp_switch\":\"yes\"}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 05:01:14', '2022-12-16 05:01:14'),
(37, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"WhatsAppbusiness\"],\"url\":[\"-\"],\"country_code\":[\"91\"],\"generateotp\":[\"Y\"],\"mobile_number\":[\"9909268997\"],\"generate_otp_switch\":\"yes\"}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 05:01:46', '2022-12-16 05:01:46'),
(38, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Instagram\"],\"url\":[\"https:\\/\\/www.instagram.com\\/accounts\\/emailsignup\\/?hl=en\"],\"country_code\":[\"91\"],\"generateotp\":[\"Y\"],\"mobile_number\":[\"9909268997\"],\"generate_otp_switch\":\"yes\"}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 05:05:19', '2022-12-16 05:05:19'),
(39, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Twitter\"],\"url\":[\"https:\\/\\/twitter.com\\/\"],\"country_code\":[\"91\"],\"generateotp\":[\"Y\"],\"mobile_number\":[\"9909268997\"],\"generate_otp_switch\":\"yes\"}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 05:06:26', '2022-12-16 05:06:26'),
(40, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Telegram\"],\"url\":[\"https:\\/\\/web.telegram.org\\/k\\/\"],\"country_code\":[\"91\"],\"generateotp\":[\"Y\"],\"mobile_number\":[\"9909268997\"],\"generate_otp_switch\":\"yes\"}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 05:07:33', '2022-12-16 05:07:33'),
(41, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Skype\"],\"url\":[\"https:\\/\\/signup.live.com\\/signup?lcid=1033&wa=wsignin1.0&rpsnv=13&ct=1661151965&rver=7.1.6819.0&wp=MBI_SSL&wreply=https%3a%2f%2flw.skype.com%2flogin%2foauth%2fproxy%3fclient_id%3d578134%26redirect_uri%3dhttps%253A%252F%252Fweb.skype.com%26source%3dscomnav%26form%3dmicrosoft_registration%26fl%3dphone2&lc=1033&id=293290&mkt=en-US&psi=skype&lw=1&cobrandid=2befc4b5-19e3-46e8-8347-77317a16a5a5&client_flight=ReservedFlight33%2CReservedFligh&fl=phone2&lic=1&uaid=b3e6be0e33d74e5283b10f2f428a84ab\"],\"country_code\":[\"91\"],\"generateotp\":[\"Y\"],\"mobile_number\":[\"9909268997\"],\"generate_otp_switch\":\"yes\"}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 05:09:05', '2022-12-16 05:09:05'),
(42, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Uber\"],\"url\":[\"drivers.uber.com\"],\"country_code\":[\"91\"],\"generateotp\":[\"N\"],\"mobile_number\":[\"9909268997\"]}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 05:11:35', '2022-12-16 05:11:35'),
(43, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Linkedin\"],\"url\":[\"https:\\/\\/www.linkedin.com\\/reg\\/join\"],\"country_code\":[\"91\"],\"generateotp\":[\"Y\"],\"mobile_number\":[\"9909268997\"],\"generate_otp_switch\":\"yes\"}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 05:12:34', '2022-12-16 05:12:34'),
(44, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Yahoo\"],\"url\":[\"https:\\/\\/login.yahoo.com\\/account\\/create?.lang=en-IN&.intl=in&.src=yhelp\"],\"country_code\":[\"91\"],\"generateotp\":[\"Y\"],\"mobile_number\":[\"9909268997\"],\"generate_otp_switch\":\"yes\"}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 05:14:35', '2022-12-16 05:14:35'),
(45, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Amazon\"],\"url\":[\"https:\\/\\/www.amazon.com\"],\"country_code\":[\"91\"],\"generateotp\":[\"Y\"],\"mobile_number\":[\"9909268997\"],\"generate_otp_switch\":\"yes\"}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 05:15:53', '2022-12-16 05:15:53'),
(46, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Microsoftteam\"],\"url\":[\"https:\\/\\/signup.live.com\\/signup?sru=https%3a%2f%2flogin.live.com%2foauth20_authorize.srf%3flc%3d1033%26mkt%3dEN-US%26opid%3dE1C4FAD9D6AF98B4%26opidt%3d1662450211%26uaid%3df7e93e1baf48418bbb681ceb04a62c04%26opignore%3d1&mkt=EN-US&uiflavor=web&lw=1&fl=easi2&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&uaid=f7e93e1baf48418bbb681ceb04a62c04&suc=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&lic=1\"],\"country_code\":[\"91\"],\"generateotp\":[\"Y\"],\"mobile_number\":[\"9909268997\"],\"generate_otp_switch\":\"yes\"}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 05:17:24', '2022-12-16 05:17:24'),
(47, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Badoo\"],\"url\":[\"https:\\/\\/badoo.com\\/signup\\/\"],\"country_code\":[\"91\"],\"generateotp\":[\"N\"],\"mobile_number\":[\"9909268997\"]}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 05:19:54', '2022-12-16 05:19:54'),
(48, 2, 'Edit', 'Brand Entry', '{\"brand_name\":\"Badoo\",\"editId\":\"36\",\"url\":\"https:\\/\\/badoo.com\\/signup\\/\",\"country_code\":\"91\",\"generateotp\":\"Y\",\"mobile_number\":\"9909268997\",\"generate_otp_switch\":\"yes\"}', 'admin/edit-save-brand-entry', '::1', 'Chrome', '2022-12-16 05:20:20', '2022-12-16 05:20:20'),
(49, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Ding\"],\"url\":[\"https:\\/\\/www.ding.com\\/register\"],\"country_code\":[\"91\"],\"generateotp\":[\"Y\"],\"mobile_number\":[\"9909268997\"],\"generate_otp_switch\":\"yes\"}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 05:21:15', '2022-12-16 05:21:15'),
(50, 2, 'Insert', 'Brand Entry', '{\"brand_name\":[\"Airbnb\"],\"url\":[\"https:\\/\\/www.airbnb.co.in\\/\"],\"country_code\":[\"91\"],\"generateotp\":[\"Y\"],\"mobile_number\":[\"9909268997\"],\"generate_otp_switch\":\"yes\"}', 'admin/add-save-brand-entry', '::1', 'Chrome', '2022-12-16 05:22:08', '2022-12-16 05:22:08'),
(51, 2, 'Delete Brand Entry', 'Brand Entry', '{\"id\":\"29\"}', 'admin/brand-entry-ajaxcall', '::1', 'Chrome', '2022-12-16 06:53:14', '2022-12-16 06:53:14'),
(52, 2, 'Edit', 'Brand Entry', '{\"brand_name\":\"Uber\",\"editId\":\"31\",\"url\":\"drivers.uber.com\",\"country_code\":\"91\",\"generateotp\":\"Y\",\"mobile_number\":\"9909268997\",\"generate_otp_switch\":\"yes\"}', 'admin/edit-save-brand-entry', '::1', 'Chrome', '2022-12-16 06:56:12', '2022-12-16 06:56:12'),
(53, 2, 'Edit', 'Brand Entry', '{\"brand_name\":\"Skype\",\"editId\":\"30\",\"url\":\"https:\\/\\/signup.live.com\\/signup?lcid=1033&wa=wsignin1.0&rpsnv=13&ct=1661151965&rver=7.1.6819.0&wp=MBI_SSL&wreply=https%3a%2f%2flw.skype.com%2flogin%2foauth%2fproxy%3fclient_id%3d578134%26redirect_uri%3dhttps%253A%252F%252Fweb.skype.com%26source%3dscomnav%26form%3dmicrosoft_registration%26fl%3dphone2&lc=1033&id=293290&mkt=en-US&psi=skype&lw=1&cobrandid=2befc4b5-19e3-46e8-8347-77317a16a5a5&client_flight=ReservedFlight33%2CReservedFligh&fl=phone2&lic=1&uaid=b3e6be0e33d74e5283b10f2f428a84ab\",\"country_code\":\"91\",\"generateotp\":\"Y\",\"mobile_number\":\"9909268997\",\"generate_otp_switch\":\"yes\"}', 'admin/edit-save-brand-entry', '::1', 'Chrome', '2022-12-16 08:54:37', '2022-12-16 08:54:37'),
(54, 2, 'Edit', 'Brand Entry', '{\"brand_name\":\"Uber\",\"editId\":\"31\",\"url\":\"https:\\/\\/auth.uber.com\\/v2\\/?breeze_local_zone=phx3&next_url=https%3A%2F%2Fdrivers.uber.com%2F&state=vpIRY6JWRP7gqQ0cA8e7JBcHwLBhgmH66jumyuUHcqg%3D\",\"country_code\":\"91\",\"generateotp\":\"Y\",\"mobile_number\":\"9909268997\",\"generate_otp_switch\":\"yes\"}', 'admin/edit-save-brand-entry', '::1', 'Chrome', '2022-12-16 09:43:29', '2022-12-16 09:43:29'),
(55, 2, 'Edit', 'Brand Entry', '{\"brand_name\":\"Badoo\",\"editId\":\"36\",\"url\":\"https:\\/\\/badoo.com\\/signup\\/\",\"country_code\":\"91\",\"generateotp\":\"Y\",\"mobile_number\":\"9909268997\",\"generate_otp_switch\":\"yes\"}', 'admin/edit-save-brand-entry', '::1', 'Chrome', '2022-12-16 09:59:51', '2022-12-16 09:59:51');

-- --------------------------------------------------------

--
-- Table structure for table `brand_entry`
--

CREATE TABLE `brand_entry` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `brand_name` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL,
  `country_code` varchar(255) DEFAULT NULL,
  `mobile_number` varchar(255) NOT NULL,
  `generate_otp` enum('Y','N') NOT NULL DEFAULT 'N' COMMENT 'Y for yes, N for no',
  `is_deleted` enum('Y','N') NOT NULL DEFAULT 'N' COMMENT 'Y for deleted, N for not deleted',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `brand_entry`
--

INSERT INTO `brand_entry` (`id`, `brand_name`, `url`, `country_code`, `mobile_number`, `generate_otp`, `is_deleted`, `created_at`, `updated_at`) VALUES
(1, 'Facebook', 'https://www.facebook.com', '91', '9428776222', 'Y', 'N', '2022-11-23 15:38:30', '2022-11-28 21:33:03'),
(2, 'Whatsapp', '-', '91', '9428776203', 'Y', 'N', '2022-11-23 15:39:13', '2022-11-23 15:39:24'),
(3, 'Google', 'https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin', '91', '9428776203', 'Y', 'N', '2022-11-29 16:20:42', '2022-11-29 16:20:42'),
(4, 'Snapchat', '-', '91', '9909267779', 'Y', 'N', '2022-12-16 04:30:45', '2022-12-16 04:31:03'),
(5, 'Hopper', '-', '91', '9427489760', 'Y', 'N', '2022-12-16 04:34:25', '2022-12-16 04:34:45'),
(6, 'Afyapap', '-', '91', '9909268558', 'Y', 'N', '2022-12-16 04:47:55', '2022-12-16 04:47:55'),
(7, 'Airbnb', '-', '91', '9909258779', 'Y', 'N', '2022-12-16 04:48:39', '2022-12-16 04:48:39'),
(8, 'Binance', '-', '91', '9909268997', 'Y', 'N', '2022-12-16 04:50:05', '2022-12-16 04:50:05'),
(9, 'Boomplay', '-', '91', '9909268997', 'Y', 'N', '2022-12-16 04:51:00', '2022-12-16 04:51:00'),
(10, 'Clubhouse', '-', '91', '9909268997', 'Y', 'N', '2022-12-16 04:51:38', '2022-12-16 04:51:38'),
(11, 'Ding', '-', '91', '9909268997', 'Y', 'N', '2022-12-16 04:52:30', '2022-12-16 04:52:30'),
(12, 'Imo', '-', '91', '9909268997', 'Y', 'N', '2022-12-16 04:53:41', '2022-12-16 04:53:41'),
(13, 'Instagram', '-', '91', '9909268997', 'Y', 'N', '2022-12-16 04:54:11', '2022-12-16 04:54:11'),
(14, 'Instagramlite', '-', '91', '9909268997', 'Y', 'N', '2022-12-16 04:54:50', '2022-12-16 04:54:50'),
(15, 'Letshego', '-', '91', '9909268997', 'Y', 'N', '2022-12-16 04:55:25', '2022-12-16 04:55:25'),
(16, 'Linkedin', '-', '91', '9909268997', 'Y', 'N', '2022-12-16 04:55:55', '2022-12-16 04:55:55'),
(17, 'Signal', '-', '91', '9909268997', 'Y', 'N', '2022-12-16 04:56:28', '2022-12-16 04:56:28'),
(18, 'Spotify', '-', '91', '9909268997', 'Y', 'N', '2022-12-16 04:57:08', '2022-12-16 04:57:08'),
(19, 'Telegram', '-', '91', '9909268997', 'Y', 'N', '2022-12-16 04:57:35', '2022-12-16 04:57:35'),
(20, 'Tinder', '-', '91', '9909268997', 'Y', 'N', '2022-12-16 04:58:09', '2022-12-16 04:58:09'),
(21, 'Truecaller', '-', '91', '9909268997', 'Y', 'N', '2022-12-16 04:58:48', '2022-12-16 04:58:48'),
(22, 'Twitter', '-', '91', '9909268997', 'Y', 'N', '2022-12-16 04:59:18', '2022-12-16 04:59:18'),
(23, 'Uber', '-', '91', '9909268997', 'Y', 'N', '2022-12-16 04:59:53', '2022-12-16 04:59:53'),
(24, 'Viber', '-', '91', '9909268997', 'Y', 'N', '2022-12-16 05:00:25', '2022-12-16 05:00:25'),
(25, 'VKMusic', '-', '91', '9909268997', 'Y', 'N', '2022-12-16 05:01:14', '2022-12-16 05:01:14'),
(26, 'WhatsAppbusiness', '-', '91', '9909268997', 'Y', 'N', '2022-12-16 05:01:46', '2022-12-16 05:01:46'),
(27, 'Instagram', 'https://www.instagram.com/accounts/emailsignup/?hl=en', '91', '9909268997', 'Y', 'N', '2022-12-16 05:05:19', '2022-12-16 05:05:19'),
(28, 'Twitter', 'https://twitter.com/', '91', '9909268997', 'Y', 'N', '2022-12-16 05:06:26', '2022-12-16 05:06:26'),
(29, 'Telegram', 'https://web.telegram.org/k/', '91', '9909268997', 'Y', 'Y', '2022-12-16 05:07:33', '2022-12-16 06:53:14'),
(30, 'Skype', 'https://signup.live.com/signup?lcid=1033&wa=wsignin1.0&rpsnv=13&ct=1661151965&rver=7.1.6819.0&wp=MBI_SSL&wreply=https%3a%2f%2flw.skype.com%2flogin%2foauth%2fproxy%3fclient_id%3d578134%26redirect_uri%3dhttps%253A%252F%252Fweb.skype.com%26source%3dscomnav%2', '91', '9909268997', 'Y', 'N', '2022-12-16 05:09:05', '2022-12-16 08:54:37'),
(31, 'Uber', 'https://auth.uber.com/v2/?breeze_local_zone=phx3&next_url=https%3A%2F%2Fdrivers.uber.com%2F&state=vpIRY6JWRP7gqQ0cA8e7JBcHwLBhgmH66jumyuUHcqg%3D', '91', '9909268997', 'Y', 'N', '2022-12-16 05:11:35', '2022-12-16 09:43:29'),
(32, 'Linkedin', 'https://www.linkedin.com/reg/join', '91', '9909268997', 'Y', 'N', '2022-12-16 05:12:34', '2022-12-16 05:12:34'),
(33, 'Yahoo', 'https://login.yahoo.com/account/create?.lang=en-IN&.intl=in&.src=yhelp', '91', '9909268997', 'Y', 'N', '2022-12-16 05:14:35', '2022-12-16 05:14:35'),
(34, 'Amazon', 'https://www.amazon.com', '91', '9909268997', 'Y', 'N', '2022-12-16 05:15:53', '2022-12-16 05:15:53'),
(35, 'Microsoftteam', 'https://signup.live.com/signup?sru=https%3a%2f%2flogin.live.com%2foauth20_authorize.srf%3flc%3d1033%26mkt%3dEN-US%26opid%3dE1C4FAD9D6AF98B4%26opidt%3d1662450211%26uaid%3df7e93e1baf48418bbb681ceb04a62c04%26opignore%3d1&mkt=EN-US&uiflavor=web&lw=1&fl=easi2&', '91', '9909268997', 'Y', 'N', '2022-12-16 05:17:24', '2022-12-16 05:17:24'),
(36, 'Badoo', 'https://badoo.com/signup/', '91', '9909268997', 'Y', 'N', '2022-12-16 05:19:54', '2022-12-16 05:20:20'),
(37, 'Ding', 'https://www.ding.com/register', '91', '9909268997', 'Y', 'N', '2022-12-16 05:21:15', '2022-12-16 05:21:15'),
(38, 'Airbnb', 'https://www.airbnb.co.in/', '91', '9909268997', 'Y', 'N', '2022-12-16 05:22:08', '2022-12-16 05:22:08');

-- --------------------------------------------------------

--
-- Table structure for table `code_number`
--

CREATE TABLE `code_number` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `no_for` varchar(255) NOT NULL,
  `number` int(11) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `countries`
--

CREATE TABLE `countries` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `shortname` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `phonecode` int(11) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `countries`
--

INSERT INTO `countries` (`id`, `shortname`, `name`, `phonecode`, `created_at`, `updated_at`) VALUES
(1, 'AF', 'Afghanistan', 93, NULL, NULL),
(2, 'AL', 'Albania', 355, NULL, NULL),
(3, 'DZ', 'Algeria', 213, NULL, NULL),
(4, 'AS', 'American Samoa', 1684, NULL, NULL),
(5, 'AD', 'Andorra', 376, NULL, NULL),
(6, 'AO', 'Angola', 244, NULL, NULL),
(7, 'AI', 'Anguilla', 1264, NULL, NULL),
(8, 'AQ', 'Antarctica', 0, NULL, NULL),
(9, 'AG', 'Antigua And Barbuda', 1268, NULL, NULL),
(10, 'AR', 'Argentina', 54, NULL, NULL),
(11, 'AM', 'Armenia', 374, NULL, NULL),
(12, 'AW', 'Aruba', 297, NULL, NULL),
(13, 'AU', 'Australia', 61, NULL, NULL),
(14, 'AT', 'Austria', 43, NULL, NULL),
(15, 'AZ', 'Azerbaijan', 994, NULL, NULL),
(16, 'BS', 'Bahamas The', 1242, NULL, NULL),
(17, 'BH', 'Bahrain', 973, NULL, NULL),
(18, 'BD', 'Bangladesh', 880, NULL, NULL),
(19, 'BB', 'Barbados', 1246, NULL, NULL),
(20, 'BY', 'Belarus', 375, NULL, NULL),
(21, 'BE', 'Belgium', 32, NULL, NULL),
(22, 'BZ', 'Belize', 501, NULL, NULL),
(23, 'BJ', 'Benin', 229, NULL, NULL),
(24, 'BM', 'Bermuda', 1441, NULL, NULL),
(25, 'BT', 'Bhutan', 975, NULL, NULL),
(26, 'BO', 'Bolivia', 591, NULL, NULL),
(27, 'BA', 'Bosnia and Herzegovina', 387, NULL, NULL),
(28, 'BW', 'Botswana', 267, NULL, NULL),
(29, 'BV', 'Bouvet Island', 0, NULL, NULL),
(30, 'BR', 'Brazil', 55, NULL, NULL),
(31, 'IO', 'British Indian Ocean Territory', 246, NULL, NULL),
(32, 'BN', 'Brunei', 673, NULL, NULL),
(33, 'BG', 'Bulgaria', 359, NULL, NULL),
(34, 'BF', 'Burkina Faso', 226, NULL, NULL),
(35, 'BI', 'Burundi', 257, NULL, NULL),
(36, 'KH', 'Cambodia', 855, NULL, NULL),
(37, 'CM', 'Cameroon', 237, NULL, NULL),
(38, 'CA', 'Canada', 1, NULL, NULL),
(39, 'CV', 'Cape Verde', 238, NULL, NULL),
(40, 'KY', 'Cayman Islands', 1345, NULL, NULL),
(41, 'CF', 'Central African Republic', 236, NULL, NULL),
(42, 'TD', 'Chad', 235, NULL, NULL),
(43, 'CL', 'Chile', 56, NULL, NULL),
(44, 'CN', 'China', 86, NULL, NULL),
(45, 'CX', 'Christmas Island', 61, NULL, NULL),
(46, 'CC', 'Cocos (Keeling) Islands', 672, NULL, NULL),
(47, 'CO', 'Colombia', 57, NULL, NULL),
(48, 'KM', 'Comoros', 269, NULL, NULL),
(49, 'CG', 'Republic Of The Congo', 242, NULL, NULL),
(50, 'CD', 'Democratic Republic Of The Congo', 242, NULL, NULL),
(51, 'CK', 'Cook Islands', 682, NULL, NULL),
(52, 'CR', 'Costa Rica', 506, NULL, NULL),
(53, 'CI', 'Cote D\'Ivoire (Ivory Coast)', 225, NULL, NULL),
(54, 'HR', 'Croatia (Hrvatska)', 385, NULL, NULL),
(55, 'CU', 'Cuba', 53, NULL, NULL),
(56, 'CY', 'Cyprus', 357, NULL, NULL),
(57, 'CZ', 'Czech Republic', 420, NULL, NULL),
(58, 'DK', 'Denmark', 45, NULL, NULL),
(59, 'DJ', 'Djibouti', 253, NULL, NULL),
(60, 'DM', 'Dominica', 1767, NULL, NULL),
(61, 'DO', 'Dominican Republic', 1809, NULL, NULL),
(62, 'TP', 'East Timor', 670, NULL, NULL),
(63, 'EC', 'Ecuador', 593, NULL, NULL),
(64, 'EG', 'Egypt', 20, NULL, NULL),
(65, 'SV', 'El Salvador', 503, NULL, NULL),
(66, 'GQ', 'Equatorial Guinea', 240, NULL, NULL),
(67, 'ER', 'Eritrea', 291, NULL, NULL),
(68, 'EE', 'Estonia', 372, NULL, NULL),
(69, 'ET', 'Ethiopia', 251, NULL, NULL),
(70, 'XA', 'External Territories of Australia', 61, NULL, NULL),
(71, 'FK', 'Falkland Islands', 500, NULL, NULL),
(72, 'FO', 'Faroe Islands', 298, NULL, NULL),
(73, 'FJ', 'Fiji Islands', 679, NULL, NULL),
(74, 'FI', 'Finland', 358, NULL, NULL),
(75, 'FR', 'France', 33, NULL, NULL),
(76, 'GF', 'French Guiana', 594, NULL, NULL),
(77, 'PF', 'French Polynesia', 689, NULL, NULL),
(78, 'TF', 'French Southern Territories', 0, NULL, NULL),
(79, 'GA', 'Gabon', 241, NULL, NULL),
(80, 'GM', 'Gambia The', 220, NULL, NULL),
(81, 'GE', 'Georgia', 995, NULL, NULL),
(82, 'DE', 'Germany', 49, NULL, NULL),
(83, 'GH', 'Ghana', 233, NULL, NULL),
(84, 'GI', 'Gibraltar', 350, NULL, NULL),
(85, 'GR', 'Greece', 30, NULL, NULL),
(86, 'GL', 'Greenland', 299, NULL, NULL),
(87, 'GD', 'Grenada', 1473, NULL, NULL),
(88, 'GP', 'Guadeloupe', 590, NULL, NULL),
(89, 'GU', 'Guam', 1671, NULL, NULL),
(90, 'GT', 'Guatemala', 502, NULL, NULL),
(91, 'XU', 'Guernsey and Alderney', 44, NULL, NULL),
(92, 'GN', 'Guinea', 224, NULL, NULL),
(93, 'GW', 'Guinea-Bissau', 245, NULL, NULL),
(94, 'GY', 'Guyana', 592, NULL, NULL),
(95, 'HT', 'Haiti', 509, NULL, NULL),
(96, 'HM', 'Heard and McDonald Islands', 0, NULL, NULL),
(97, 'HN', 'Honduras', 504, NULL, NULL),
(98, 'HK', 'Hong Kong S.A.R.', 852, NULL, NULL),
(99, 'HU', 'Hungary', 36, NULL, NULL),
(100, 'IS', 'Iceland', 354, NULL, NULL),
(101, 'IN', 'India', 91, NULL, NULL),
(102, 'ID', 'Indonesia', 62, NULL, NULL),
(103, 'IR', 'Iran', 98, NULL, NULL),
(104, 'IQ', 'Iraq', 964, NULL, NULL),
(105, 'IE', 'Ireland', 353, NULL, NULL),
(106, 'IL', 'Israel', 972, NULL, NULL),
(107, 'IT', 'Italy', 39, NULL, NULL),
(108, 'JM', 'Jamaica', 1876, NULL, NULL),
(109, 'JP', 'Japan', 81, NULL, NULL),
(110, 'XJ', 'Jersey', 44, NULL, NULL),
(111, 'JO', 'Jordan', 962, NULL, NULL),
(112, 'KZ', 'Kazakhstan', 7, NULL, NULL),
(113, 'KE', 'Kenya', 254, NULL, NULL),
(114, 'KI', 'Kiribati', 686, NULL, NULL),
(115, 'KP', 'Korea North', 850, NULL, NULL),
(116, 'KR', 'Korea South', 82, NULL, NULL),
(117, 'KW', 'Kuwait', 965, NULL, NULL),
(118, 'KG', 'Kyrgyzstan', 996, NULL, NULL),
(119, 'LA', 'Laos', 856, NULL, NULL),
(120, 'LV', 'Latvia', 371, NULL, NULL),
(121, 'LB', 'Lebanon', 961, NULL, NULL),
(122, 'LS', 'Lesotho', 266, NULL, NULL),
(123, 'LR', 'Liberia', 231, NULL, NULL),
(124, 'LY', 'Libya', 218, NULL, NULL),
(125, 'LI', 'Liechtenstein', 423, NULL, NULL),
(126, 'LT', 'Lithuania', 370, NULL, NULL),
(127, 'LU', 'Luxembourg', 352, NULL, NULL),
(128, 'MO', 'Macau S.A.R.', 853, NULL, NULL),
(129, 'MK', 'Macedonia', 389, NULL, NULL),
(130, 'MG', 'Madagascar', 261, NULL, NULL),
(131, 'MW', 'Malawi', 265, NULL, NULL),
(132, 'MY', 'Malaysia', 60, NULL, NULL),
(133, 'MV', 'Maldives', 960, NULL, NULL),
(134, 'ML', 'Mali', 223, NULL, NULL),
(135, 'MT', 'Malta', 356, NULL, NULL),
(136, 'XM', 'Man (Isle of)', 44, NULL, NULL),
(137, 'MH', 'Marshall Islands', 692, NULL, NULL),
(138, 'MQ', 'Martinique', 596, NULL, NULL),
(139, 'MR', 'Mauritania', 222, NULL, NULL),
(140, 'MU', 'Mauritius', 230, NULL, NULL),
(141, 'YT', 'Mayotte', 269, NULL, NULL),
(142, 'MX', 'Mexico', 52, NULL, NULL),
(143, 'FM', 'Micronesia', 691, NULL, NULL),
(144, 'MD', 'Moldova', 373, NULL, NULL),
(145, 'MC', 'Monaco', 377, NULL, NULL),
(146, 'MN', 'Mongolia', 976, NULL, NULL),
(147, 'MS', 'Montserrat', 1664, NULL, NULL),
(148, 'MA', 'Morocco', 212, NULL, NULL),
(149, 'MZ', 'Mozambique', 258, NULL, NULL),
(150, 'MM', 'Myanmar', 95, NULL, NULL),
(151, 'NA', 'Namibia', 264, NULL, NULL),
(152, 'NR', 'Nauru', 674, NULL, NULL),
(153, 'NP', 'Nepal', 977, NULL, NULL),
(154, 'AN', 'Netherlands Antilles', 599, NULL, NULL),
(155, 'NL', 'Netherlands The', 31, NULL, NULL),
(156, 'NC', 'New Caledonia', 687, NULL, NULL),
(157, 'NZ', 'New Zealand', 64, NULL, NULL),
(158, 'NI', 'Nicaragua', 505, NULL, NULL),
(159, 'NE', 'Niger', 227, NULL, NULL),
(160, 'NG', 'Nigeria', 234, NULL, NULL),
(161, 'NU', 'Niue', 683, NULL, NULL),
(162, 'NF', 'Norfolk Island', 672, NULL, NULL),
(163, 'MP', 'Northern Mariana Islands', 1670, NULL, NULL),
(164, 'NO', 'Norway', 47, NULL, NULL),
(165, 'OM', 'Oman', 968, NULL, NULL),
(166, 'PK', 'Pakistan', 92, NULL, NULL),
(167, 'PW', 'Palau', 680, NULL, NULL),
(168, 'PS', 'Palestinian Territory Occupied', 970, NULL, NULL),
(169, 'PA', 'Panama', 507, NULL, NULL),
(170, 'PG', 'Papua new Guinea', 675, NULL, NULL),
(171, 'PY', 'Paraguay', 595, NULL, NULL),
(172, 'PE', 'Peru', 51, NULL, NULL),
(173, 'PH', 'Philippines', 63, NULL, NULL),
(174, 'PN', 'Pitcairn Island', 0, NULL, NULL),
(175, 'PL', 'Poland', 48, NULL, NULL),
(176, 'PT', 'Portugal', 351, NULL, NULL),
(177, 'PR', 'Puerto Rico', 1787, NULL, NULL),
(178, 'QA', 'Qatar', 974, NULL, NULL),
(179, 'RE', 'Reunion', 262, NULL, NULL),
(180, 'RO', 'Romania', 40, NULL, NULL),
(181, 'RU', 'Russia', 70, NULL, NULL),
(182, 'RW', 'Rwanda', 250, NULL, NULL),
(183, 'SH', 'Saint Helena', 290, NULL, NULL),
(184, 'KN', 'Saint Kitts And Nevis', 1869, NULL, NULL),
(185, 'LC', 'Saint Lucia', 1758, NULL, NULL),
(186, 'PM', 'Saint Pierre and Miquelon', 508, NULL, NULL),
(187, 'VC', 'Saint Vincent And The Grenadines', 1784, NULL, NULL),
(188, 'WS', 'Samoa', 684, NULL, NULL),
(189, 'SM', 'San Marino', 378, NULL, NULL),
(190, 'ST', 'Sao Tome and Principe', 239, NULL, NULL),
(191, 'SA', 'Saudi Arabia', 966, NULL, NULL),
(192, 'SN', 'Senegal', 221, NULL, NULL),
(193, 'RS', 'Serbia', 381, NULL, NULL),
(194, 'SC', 'Seychelles', 248, NULL, NULL),
(195, 'SL', 'Sierra Leone', 232, NULL, NULL),
(196, 'SG', 'Singapore', 65, NULL, NULL),
(197, 'SK', 'Slovakia', 421, NULL, NULL),
(198, 'SI', 'Slovenia', 386, NULL, NULL),
(199, 'XG', 'Smaller Territories of the UK', 44, NULL, NULL),
(200, 'SB', 'Solomon Islands', 677, NULL, NULL),
(201, 'SO', 'Somalia', 252, NULL, NULL),
(202, 'ZA', 'South Africa', 27, NULL, NULL),
(203, 'GS', 'South Georgia', 0, NULL, NULL),
(204, 'SS', 'South Sudan', 211, NULL, NULL),
(205, 'ES', 'Spain', 34, NULL, NULL),
(206, 'LK', 'Sri Lanka', 94, NULL, NULL),
(207, 'SD', 'Sudan', 249, NULL, NULL),
(208, 'SR', 'Suriname', 597, NULL, NULL),
(209, 'SJ', 'Svalbard And Jan Mayen Islands', 47, NULL, NULL),
(210, 'SZ', 'Swaziland', 268, NULL, NULL),
(211, 'SE', 'Sweden', 46, NULL, NULL),
(212, 'CH', 'Switzerland', 41, NULL, NULL),
(213, 'SY', 'Syria', 963, NULL, NULL),
(214, 'TW', 'Taiwan', 886, NULL, NULL),
(215, 'TJ', 'Tajikistan', 992, NULL, NULL),
(216, 'TZ', 'Tanzania', 255, NULL, NULL),
(217, 'TH', 'Thailand', 66, NULL, NULL),
(218, 'TG', 'Togo', 228, NULL, NULL),
(219, 'TK', 'Tokelau', 690, NULL, NULL),
(220, 'TO', 'Tonga', 676, NULL, NULL),
(221, 'TT', 'Trinidad And Tobago', 1868, NULL, NULL),
(222, 'TN', 'Tunisia', 216, NULL, NULL),
(223, 'TR', 'Turkey', 90, NULL, NULL),
(224, 'TM', 'Turkmenistan', 7370, NULL, NULL),
(225, 'TC', 'Turks And Caicos Islands', 1649, NULL, NULL),
(226, 'TV', 'Tuvalu', 688, NULL, NULL),
(227, 'UG', 'Uganda', 256, NULL, NULL),
(228, 'UA', 'Ukraine', 380, NULL, NULL),
(229, 'AE', 'United Arab Emirates', 971, NULL, NULL),
(230, 'GB', 'United Kingdom', 44, NULL, NULL),
(231, 'US', 'United States', 1, NULL, NULL),
(232, 'UM', 'United States Minor Outlying Islands', 1, NULL, NULL),
(233, 'UY', 'Uruguay', 598, NULL, NULL),
(234, 'UZ', 'Uzbekistan', 998, NULL, NULL),
(235, 'VU', 'Vanuatu', 678, NULL, NULL),
(236, 'VA', 'Vatican City State (Holy See)', 39, NULL, NULL),
(237, 'VE', 'Venezuela', 58, NULL, NULL),
(238, 'VN', 'Vietnam', 84, NULL, NULL),
(239, 'VG', 'Virgin Islands (British)', 1284, NULL, NULL),
(240, 'VI', 'Virgin Islands (US)', 1340, NULL, NULL),
(241, 'WF', 'Wallis And Futuna Islands', 681, NULL, NULL),
(242, 'EH', 'Western Sahara', 212, NULL, NULL),
(243, 'YE', 'Yemen', 967, NULL, NULL),
(244, 'YU', 'Yugoslavia', 38, NULL, NULL),
(245, 'ZM', 'Zambia', 260, NULL, NULL),
(246, 'ZW', 'Zimbabwe', 263, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `device`
--

CREATE TABLE `device` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `device_name` varchar(255) NOT NULL,
  `add_by` int(11) NOT NULL,
  `updated_by` int(11) NOT NULL,
  `status` enum('A','I') NOT NULL DEFAULT 'A' COMMENT 'A for Active, I for not Inactive',
  `is_deleted` enum('Y','N') NOT NULL DEFAULT 'N' COMMENT 'Y for deleted, N for not deleted',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `device`
--

INSERT INTO `device` (`id`, `device_name`, `add_by`, `updated_by`, `status`, `is_deleted`, `created_at`, `updated_at`) VALUES
(1, 'samsung', 2, 2, 'A', 'N', '2022-11-28 19:49:57', '2022-11-28 19:49:57');

-- --------------------------------------------------------

--
-- Table structure for table `migrations`
--

CREATE TABLE `migrations` (
  `id` int(10) UNSIGNED NOT NULL,
  `migration` varchar(255) NOT NULL,
  `batch` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `migrations`
--

INSERT INTO `migrations` (`id`, `migration`, `batch`) VALUES
(1, '2014_10_12_000000_create_users_table', 1),
(2, '2019_12_14_000001_create_personal_access_tokens_table', 1),
(3, '2022_01_06_182648_create_user_type_table', 1),
(4, '2022_01_24_181032_create_audit_trails_table', 1),
(5, '2022_01_26_061619_create_system_setting_table', 1),
(6, '2022_01_26_101956_create_smtp_setting_table', 1),
(7, '2022_04_22_142232_create_code_number_table', 1),
(8, '2022_04_26_131700_create_brand_entry_table', 1),
(9, '2022_04_26_132920_add_is_deleted_brand_entry_table', 1),
(10, '2022_04_27_125435_change_brand_entry_table', 1),
(11, '2022_04_27_134316_create_result_reports_table', 1),
(12, '2022_06_13_062421_create_user_management_table', 1),
(13, '2022_06_13_064004_drop_user_type_users_table', 1),
(14, '2022_06_13_064320_add_user_type_users_table', 1),
(15, '2022_06_13_113156_add_user_no_users_table', 1),
(16, '2022_06_13_115859_create_device_table', 1),
(17, '2022_06_13_134755_create_country_table', 1),
(18, '2022_06_13_135915_drop_country_table', 1),
(19, '2022_06_13_141622_create_mobile_number_table', 1),
(20, '2022_06_13_142027_add_is_deleted_mobile_number_table', 1),
(21, '2022_06_14_104826_create_run_script_table', 1),
(22, '2022_06_14_105836_add_deviceis_run_script_table', 1),
(23, '2022_06_17_071548_drop_run_script_table', 1),
(24, '2022_06_20_083531_add_theme_colors_systemsetting_table', 1),
(25, '2022_06_27_055442_create_users_report_table', 1),
(26, '2022_08_03_132906_add_number_table', 1),
(27, '2022_08_04_075519_drop_col_result_reports_table', 1),
(28, '2022_08_04_075658_add_new_col_result_reports_table', 1),
(29, '2022_08_04_094434_add_sender_address_result_reports_table', 1),
(30, '2022_11_24_120837_add_is_used_mobile_number_table', 2);

-- --------------------------------------------------------

--
-- Table structure for table `mobile_number`
--

CREATE TABLE `mobile_number` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `number` varchar(255) DEFAULT NULL,
  `country_id` int(11) NOT NULL,
  `mobile_number` varchar(255) NOT NULL,
  `operator` varchar(255) NOT NULL,
  `is_used` enum('N','Y') NOT NULL DEFAULT 'N' COMMENT 'Y for IN use, N for Not use',
  `add_by` int(11) NOT NULL,
  `updated_by` int(11) NOT NULL,
  `status` enum('A','I') NOT NULL DEFAULT 'A' COMMENT 'A for Active, I for not Inactive',
  `is_deleted` enum('Y','N') NOT NULL DEFAULT 'N' COMMENT 'Y for deleted, N for not deleted',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `mobile_number`
--

INSERT INTO `mobile_number` (`id`, `number`, `country_id`, `mobile_number`, `operator`, `is_used`, `add_by`, `updated_by`, `status`, `is_deleted`, `created_at`, `updated_at`) VALUES
(1, '+919824345559', 101, '9824345559', 'jio', 'N', 2, 2, 'A', 'N', '2022-11-28 19:48:10', '2022-11-28 19:48:10');

-- --------------------------------------------------------

--
-- Table structure for table `personal_access_tokens`
--

CREATE TABLE `personal_access_tokens` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `tokenable_type` varchar(255) NOT NULL,
  `tokenable_id` bigint(20) UNSIGNED NOT NULL,
  `name` varchar(255) NOT NULL,
  `token` varchar(64) NOT NULL,
  `abilities` text DEFAULT NULL,
  `last_used_at` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `result_reports`
--

CREATE TABLE `result_reports` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `uuid` varchar(255) DEFAULT NULL,
  `smsid` varchar(255) DEFAULT NULL,
  `event_time` datetime NOT NULL,
  `brand` varchar(255) DEFAULT NULL,
  `sender_address` varchar(255) DEFAULT NULL,
  `recipient_msisdn` varchar(255) DEFAULT NULL,
  `sccp_gt` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `received_content` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `result_reports`
--

INSERT INTO `result_reports` (`id`, `uuid`, `smsid`, `event_time`, `brand`, `sender_address`, `recipient_msisdn`, `sccp_gt`, `status`, `received_content`, `created_at`, `updated_at`) VALUES
(1, '1234', '1234', '2022-08-01 15:15:54', NULL, 'Snapchat', NULL, '+9182999019999', NULL, '<#> Snapchat Code: 283288. Happy Sanpping! quanty57f5Rf', '2022-12-12 15:44:04', '2022-12-12 15:44:04'),
(2, '57bcb349dc12de47', '468', '2022-12-12 13:31:51', NULL, '59039200', '+919113236861', '+918299901123', NULL, '<#> 815 740 is your Instagram code. Don\'t share it. SIYRxKrru1t', '2022-12-12 16:01:52', '2022-12-12 16:01:52'),
(3, 'b3eaf388553dc4aa', '12737', '2022-12-12 12:35:21', NULL, 'Airtel', '+260978981289', '+260971911214', NULL, 'Test message', '2022-12-12 18:35:24', '2022-12-12 18:35:24'),
(4, 'b3eaf388553dc4aa', '12739', '2022-12-12 14:32:06', NULL, 'Airtel Data', '+260978981289', '+260971911215', NULL, 'Successfully subscribed to 1day 100MB Tonse Data Bundle. Your new volume is 100.00MB.The latest bought bundle is valid until 13-12-2022 14:32.', '2022-12-12 20:32:09', '2022-12-12 20:32:09'),
(5, 'b3eaf388553dc4aa', '12744', '2022-12-12 14:50:16', NULL, 'AirtelMoney', '+260978981289', '+260971911215', NULL, 'Txn. ID : LP221212.1450.G77550. Payment to AMMOBILE Account NA of ZMW 10.00 is successful. Your Airtel Money balance is ZMW 26.84', '2022-12-12 20:52:07', '2022-12-12 20:52:07'),
(6, 'b3eaf388553dc4aa', '12745', '2022-12-12 14:52:01', NULL, 'Airtel', '+260978981289', '+260971911214', NULL, 'Your Beep call request was successful.', '2022-12-12 20:52:52', '2022-12-12 20:52:52'),
(7, 'b3eaf388553dc4aa', '12746', '2022-12-12 14:52:50', NULL, 'Soche', '+260978981289', '+260971911215', NULL, 'Use NEW short code *117# to buy Minutes. Thank you for buying K2.0 Pack giving you 9Min, 100SMS . Valid till 13-12-2022 14:52 To check balance dial *117*14#.', '2022-12-12 20:52:55', '2022-12-12 20:52:55'),
(8, 'b3eaf388553dc4aa', '12749', '2022-12-12 15:11:08', NULL, 'Airtel Data', '+260978981289', '+260971911214', NULL, 'You have depleted one of your Tonse bundles.To check total balance or buy topup bundles Dial *117#,then 4 or Click https://bit.ly/2keYWN1 for AirtelApp', '2022-12-12 21:11:11', '2022-12-12 21:11:11'),
(9, 'a0cc9c5fedc0d9dd', '104', '2022-12-12 15:36:15', NULL, 'WhatsApp', '+260950003776', '+46721497400', NULL, '<#> Your WhatsApp code: 514-023\n\nYou can also tap on this link to verify your phone: v.whatsapp.com/514023\n\nDon\'t share this code with others\n4sgLq1p5sV6', '2022-12-12 21:36:16', '2022-12-12 21:36:16'),
(10, 'a0cc9c5fedc0d9dd', '105', '2022-12-12 17:12:26', NULL, 'MTNZM', '+260950003776', '+26096060815', NULL, 'Y’ello. You have used up 90% of your 8704 MB data bundle. Dial *335# to buy another bundle.', '2022-12-12 23:12:27', '2022-12-12 23:12:27'),
(11, 'a0cc9c5fedc0d9dd', '106', '2022-12-12 20:21:25', NULL, '+260973972173', '+260950003776', '+260971911248', NULL, 'Am asking for mobile money? Please', '2022-12-13 02:21:28', '2022-12-13 02:21:28'),
(12, 'b3eaf388553dc4aa', '12751', '2022-12-13 07:29:52', NULL, 'NAPSA', '+260978981289', '+26095199004', NULL, 'A NAPSA contribution of K 2,443.60 for Nov-2022 has been posted to your account. Dial 677, or WhatsApp 0973000677 to report any anomaly', '2022-12-13 13:29:55', '2022-12-13 13:29:55'),
(13, 'b3eaf388553dc4aa', '12753', '2022-12-13 08:25:16', NULL, 'AirtelMoney', '+260978981289', '+260971911215', NULL, 'Txn. ID : ES221213.0825.N16540. You currently have ZMW 32.84 available on your account.', '2022-12-13 14:25:20', '2022-12-13 14:25:20'),
(14, 'b3eaf388553dc4aa', '12756', '2022-12-13 10:12:16', NULL, 'Airtel', '+260978981289', '+260971911214', NULL, 'Dear Customer, You can now move money from your FNB bank account to your Airtel Money Wallet. Its Instant, Secure and Easy. Simply Dial *130*321# to start.', '2022-12-13 16:12:27', '2022-12-13 16:12:27'),
(15, 'b3eaf388553dc4aa', '12757', '2022-12-13 10:26:10', NULL, 'Airtel Data', '+260978981289', '+260971911214', NULL, 'You have used 90% of one of your Ikali bundles.To check total balance or buy topup bundles Dial *117#,then 4 or Click https://bit.ly/2keYWN1 for AirtelApp', '2022-12-13 16:26:14', '2022-12-13 16:26:14'),
(16, 'b3eaf388553dc4aa', '12758', '2022-12-13 10:42:03', NULL, 'Airtel', '+260978981289', '+260971911214', NULL, 'Dear Customer, You can now move money from your ABSA bank account to your Airtel Money Wallet. Its Instant, Secure and Easy. Simply Dial *229# to start.', '2022-12-13 16:42:05', '2022-12-13 16:42:05'),
(17, 'b3eaf388553dc4aa', '12759', '2022-12-13 11:30:01', NULL, 'Absa', '+260978981289', '+260971911214', NULL, 'Dear Mwansa, Do all your digital banking from the comfort of your home. Dial *229# to send cash, pay bills, buy airtime, check balances & much more.', '2022-12-13 17:30:06', '2022-12-13 17:30:06'),
(18, 'b3eaf388553dc4aa', '12760', '2022-12-13 11:38:38', NULL, 'AirtelMoney', '+260978981289', '+260971911215', NULL, 'Dear Customer, you have received ZMW 200.00 from 977292392 chrispin mulenga. Dial *115# to check your new balance. Txn ID: PP221213.1138.M45781.', '2022-12-13 17:38:42', '2022-12-13 17:38:42'),
(19, 'b3eaf388553dc4aa', '12761', '2022-12-13 11:49:10', NULL, 'AirtelMoney', '+260978981289', '+260971911215', NULL, 'Use NEW short code *115# for Airtel Money. You have withdrawn ZMW 100.00 from 976830331 Friday Siwakwi. Your balance is ZMW 101.34. Txn. ID: CO221213.1148.L32842.', '2022-12-13 17:49:20', '2022-12-13 17:49:20'),
(20, 'a0cc9c5fedc0d9dd', '110', '2022-12-13 13:35:24', NULL, 'WhatsApp', '+260950003776', '+46721497100', NULL, '<#> Your WhatsApp code: 818-847\n\nYou can also tap on this link to verify your phone: v.whatsapp.com/818847\n\nDon\'t share this code with others\n4sgLq1p5sV6', '2022-12-13 19:35:37', '2022-12-13 19:35:37'),
(21, 'a0cc9c5fedc0d9dd', '111', '2022-12-13 13:46:49', NULL, 'Google', '+260950003776', '+46721497100', NULL, 'G-921200 is your Google verification code.', '2022-12-13 19:46:52', '2022-12-13 19:46:52'),
(22, 'a0cc9c5fedc0d9dd', '112', '2022-12-13 13:47:47', NULL, 'Twitter', '+260950003776', '+46721497100', NULL, 'Your Twitter confirmation code is 062705.', '2022-12-13 19:47:48', '2022-12-13 19:47:48'),
(23, 'a0cc9c5fedc0d9dd', '113', '2022-12-13 13:51:19', NULL, 'Facebook', '+260950003776', '+46721497100', NULL, '718 640 is your Instagram code. Don\'t share it.', '2022-12-13 19:51:21', '2022-12-13 19:51:21'),
(24, 'a0cc9c5fedc0d9dd', '114', '2022-12-13 13:53:50', NULL, 'HUAWEI', '+260950003776', '+46721497100', NULL, '651880 - Huawei verification code to register HUAWEI ID.', '2022-12-13 19:53:52', '2022-12-13 19:53:52'),
(25, 'a0cc9c5fedc0d9dd', '115', '2022-12-13 13:55:39', NULL, 'Phone Code', '+260950003776', '+46721497400', NULL, '847278 is your verification code for web.cashbook.in.', '2022-12-13 19:55:41', '2022-12-13 19:55:41'),
(26, 'a0cc9c5fedc0d9dd', '116', '2022-12-13 13:56:01', NULL, 'Viber', '+260950003776', '+46721497100', NULL, '<#> Your Viber code: 553539\n\nYou can also tap this link to finish your activation:\nhttps://unv.viber.com/a/553539\n\n6EQbNfKgO8O', '2022-12-13 19:56:02', '2022-12-13 19:56:02'),
(27, 'a0cc9c5fedc0d9dd', '117', '2022-12-13 13:59:37', NULL, 'Uber', '+260950003776', '+46721497100', NULL, 'Your Uber code is 7313. Never share this code. qlRnn4A1sbt', '2022-12-13 19:59:39', '2022-12-13 19:59:39'),
(28, 'a0cc9c5fedc0d9dd', '118', '2022-12-13 14:00:59', NULL, 'note', '+260950003776', '+26095199004', NULL, 'Here is the cde 711961', '2022-12-13 20:01:01', '2022-12-13 20:01:01'),
(29, 'a0cc9c5fedc0d9dd', '126', '2022-12-13 15:00:47', NULL, 'Uber', '+260950003776', '+46721497100', NULL, 'Your Uber code is 0335. Never share this code. Reply STOP ALL to +1 415-237-0403 to unsubscribe. qlRnn4A1sbt', '2022-12-13 21:00:50', '2022-12-13 21:00:50'),
(30, 'a0cc9c5fedc0d9dd', '127', '2022-12-13 15:02:28', NULL, 'SIGNAL', '+260950003776', '+46721497100', NULL, 'Your SIGNAL verification code is: 881354\ndoDiFGKPO1r', '2022-12-13 21:02:30', '2022-12-13 21:02:30'),
(31, 'a0cc9c5fedc0d9dd', '128', '2022-12-13 15:07:06', NULL, 'Uber', '+260950003776', '+46721497400', NULL, 'Your Uber code is 0335. Never share this code. Reply STOP ALL to +1 415-237-0403 to unsubscribe. qlRnn4A1sbt', '2022-12-13 21:07:07', '2022-12-13 21:07:07'),
(32, 'b3eaf388553dc4aa', '12768', '2022-12-13 15:09:11', NULL, 'Ikali', '+260978981289', '+260971911215', NULL, 'Use NEW short code *117# to buy Ikali. Thank you for choosing Ikali. You have purchased a Daily pack of 1.20GB of Data valid until 14-12-2022 15:09', '2022-12-13 21:09:15', '2022-12-13 21:09:15'),
(33, 'a0cc9c5fedc0d9dd', '129', '2022-12-13 15:12:55', NULL, 'Facebook', '+260950003776', '+46721497100', NULL, '40190 is your Facebook confirmation code', '2022-12-13 21:12:57', '2022-12-13 21:12:57'),
(34, 'a0cc9c5fedc0d9dd', '130', '2022-12-13 15:14:09', NULL, 'xiaomi', '+260950003776', '+46721497400', NULL, 'Mi Account verification code: 069382. It expires in 5 minutes.', '2022-12-13 21:14:11', '2022-12-13 21:14:11'),
(35, 'a0cc9c5fedc0d9dd', '131', '2022-12-13 15:14:50', NULL, 'TINDER', '+260950003776', '+46721497100', NULL, 'Your Tinder code is 785723 Don’t share @tinder.com #785723', '2022-12-13 21:14:52', '2022-12-13 21:14:52'),
(36, 'a0cc9c5fedc0d9dd', '132', '2022-12-13 15:15:32', NULL, 'VKcom', '+260950003776', '+46721497100', NULL, 'VK: 454065 - your code', '2022-12-13 21:15:47', '2022-12-13 21:15:47'),
(37, 'a0cc9c5fedc0d9dd', '133', '2022-12-13 15:17:21', NULL, 'Microsoft', '+260950003776', '+46721497100', NULL, 'Use 3420 as Microsoft account security code. Go passwordless with Microsoft Authenticator https://aka.ms/authapp', '2022-12-13 21:17:23', '2022-12-13 21:17:23'),
(38, 'a0cc9c5fedc0d9dd', '134', '2022-12-13 15:18:50', NULL, 'Twitter', '+260950003776', '+46721497400', NULL, 'Your Twitter confirmation code is 961338.', '2022-12-13 21:18:52', '2022-12-13 21:18:52'),
(39, 'a0cc9c5fedc0d9dd', '135', '2022-12-13 15:21:06', NULL, 'SIGNAL', '+260950003776', '+46721497100', NULL, 'Your SIGNAL verification code is: 636360\ndoDiFGKPO1r', '2022-12-13 21:21:08', '2022-12-13 21:21:08'),
(40, 'a0cc9c5fedc0d9dd', '136', '2022-12-13 15:21:13', NULL, 'note', '+260950003776', '+26095199004', NULL, 'Login Key - 697533', '2022-12-13 21:21:15', '2022-12-13 21:21:15'),
(41, 'a0cc9c5fedc0d9dd', '137', '2022-12-13 15:25:02', NULL, 'Binance', '+260950003776', '+46721497100', NULL, 'Your Binance login verification code: 729185. Do not share this code with anyone. Visit your Binance account now.', '2022-12-13 21:25:04', '2022-12-13 21:25:04'),
(42, 'b3eaf388553dc4aa', '12770', '2022-12-13 18:26:09', NULL, 'Soche', '+260978981289', '+260971911215', NULL, 'Use NEW short code *117# to buy Minutes. Thank you for buying K5.0 Pack giving you 36Min, 250SMS and 20MB. Valid till 14-12-2022 18:26 To check balance dial *117*14#.', '2022-12-14 00:26:11', '2022-12-14 00:26:11'),
(43, 'b3eaf388553dc4aa', '12770', '2022-12-13 18:26:09', NULL, 'Soche', '+260978981289', '+260971911215', NULL, 'Use NEW short code *117# to buy Minutes. Thank you for buying K5.0 Pack giving you 36Min, 250SMS and 20MB. Valid till 14-12-2022 18:26 To check balance dial *117*14#.', '2022-12-14 00:26:11', '2022-12-14 00:26:11'),
(44, 'a0cc9c5fedc0d9dd', '138', '2022-12-13 19:33:20', NULL, '+260973972173', '+260950003776', '+260971911248', NULL, 'One return visit and 8 hours', '2022-12-14 01:33:21', '2022-12-14 01:33:21'),
(45, 'b3eaf388553dc4aa', '12771', '2022-12-13 18:26:11', NULL, 'AirtelMoney', '+260978981289', '+260971911215', NULL, 'Txn. ID : LP221213.1826.I49067. Payment to AMMOBILE Account NA of ZMW 5.00 is successful. Your Airtel Money balance is ZMW 84.34', '2022-12-14 01:48:19', '2022-12-14 01:48:19'),
(46, 'b3eaf388553dc4aa', '12773', '2022-12-14 01:14:32', NULL, 'Absa', '+260978981289', '+260971911214', NULL, 'The balance on your account ending 0522 is ZMW 19.85 as of 13 Dec 2022', '2022-12-14 07:14:36', '2022-12-14 07:14:36'),
(47, 'b3eaf388553dc4aa', '12775', '2022-12-14 06:06:21', NULL, 'Absa', '+260978981289', '+260971911214', NULL, 'Dear Customer available balance for use on your credit card XXXXXXXXXXXX0820 on 2022-12-13 is ZMW -184.43. Thank you. For any enquires call +260211366 223', '2022-12-14 14:37:15', '2022-12-14 14:37:15'),
(48, 'b3eaf388553dc4aa', '12778', '2022-12-14 08:55:34', NULL, 'Soche', '+260978981289', '+260971911215', NULL, 'Use NEW short code *117# to buy Minutes. Thank you for buying K5.0 Pack giving you 26Min, 250SMS and 20MB. Valid till 15-12-2022 08:55 To check balance dial *117*14#.', '2022-12-14 14:55:38', '2022-12-14 14:55:38'),
(49, 'b3eaf388553dc4aa', '12781', '2022-12-14 09:57:11', NULL, 'Siliza', '+260978981289', '+260971911214', NULL, 'Dear Customer, you have been credited with K3.00 airtime. Please recharge by 16.12.2022 with K3.30 to repay your advance. T\'s and C\'s apply.', '2022-12-14 15:57:15', '2022-12-14 15:57:15'),
(50, 'b3eaf388553dc4aa', '12785', '2022-12-14 10:03:19', NULL, '878', '+260978981289', '+260971911214', NULL, 'Service is expired', '2022-12-14 16:03:23', '2022-12-14 16:03:23'),
(51, 'a0cc9c5fedc0d9dd', '139', '2022-12-14 10:53:21', NULL, 'FRAUD', '+260950003776', '+26095199004', NULL, 'Hello! The festive season is here. Enjoy your digital services responsibly. Beware of scammers! Dial *707# to report all scams.', '2022-12-14 16:53:22', '2022-12-14 16:53:22'),
(52, 'b3eaf388553dc4aa', '12788', '2022-12-14 11:01:50', NULL, 'FACEBOOK', '+260978981289', '+918299901900', NULL, '45886 is your Facebook confirmation code', '2022-12-14 17:01:53', '2022-12-14 17:01:53'),
(53, 'b3eaf388553dc4aa', '12789', '2022-12-14 11:04:17', NULL, 'FACEBOOK', '+260978981289', '+918299901900', NULL, '45886 is your Facebook confirmation code', '2022-12-14 17:04:19', '2022-12-14 17:04:19'),
(54, 'b3eaf388553dc4aa', '12791', '2022-12-14 11:06:29', NULL, 'CloudOTP', '+260978981289', '+918299901900', NULL, '992253 is your verification code for web.cashbook.in.', '2022-12-14 17:06:31', '2022-12-14 17:06:31'),
(55, 'b3eaf388553dc4aa', '12793', '2022-12-14 11:12:34', NULL, 'FACEBOOK', '+260978981289', '+918299901900', NULL, '276 158 is your Instagram code. Don\'t share it.', '2022-12-14 17:12:37', '2022-12-14 17:12:37'),
(56, 'b3eaf388553dc4aa', '12794', '2022-12-14 11:15:07', NULL, 'URBAN', '+260978981289', '+260971911214', NULL, '4842 is your OTP. Kindly use it within 2 minutes else it will expire - URBN', '2022-12-14 17:18:03', '2022-12-14 17:18:03'),
(57, 'b3eaf388553dc4aa', '12795', '2022-12-14 11:18:01', NULL, 'TINDER', '+260978981289', '+918299901900', NULL, 'Your Tinder code is 618765 Don\'t share @tinder.com #618765', '2022-12-14 17:20:17', '2022-12-14 17:20:17'),
(58, 'b3eaf388553dc4aa', '12796', '2022-12-14 11:20:15', NULL, 'AIRBNB', '+260978981289', '+918299901900', NULL, 'Your Airbnb verification code is: 490279. Don\'t share this code with anyone; our employees will never ask for the code.', '2022-12-14 17:21:14', '2022-12-14 17:21:14'),
(59, 'b3eaf388553dc4aa', '12797', '2022-12-14 11:21:13', NULL, 'AUTHMSG', '+260978981289', '+918299901900', NULL, 'Your Airbnb verification code is: 985174. Don\'t share this code with anyone; our employees will never ask for the code.', '2022-12-14 17:24:23', '2022-12-14 17:24:23'),
(60, 'b3eaf388553dc4aa', '12799', '2022-12-14 11:26:53', NULL, 'Viber', '+260978981289', '+918299901900', NULL, '<#> Your Viber code: 603879\n\nYou can also tap this link to finish your activation:\nhttps://unv.viber.com/a/603879\n\n6EQbNfKgO8O', '2022-12-14 17:26:57', '2022-12-14 17:26:57'),
(61, 'b3eaf388553dc4aa', '12800', '2022-12-14 11:28:56', NULL, 'Telegram', '+260978981289', '+918299901900', NULL, 'Telegram code: 13287\n\nYou can also tap on this link to log in:\nhttps://t.me/login/13287\n\noLeq9AcOZkT', '2022-12-14 17:31:35', '2022-12-14 17:31:35'),
(62, 'b3eaf388553dc4aa', '12802', '2022-12-14 11:35:21', NULL, 'Yandex', '+260978981289', '+918299901900', NULL, 'Your confirmation code is 235-735. Please enter it in the text field.', '2022-12-14 17:35:26', '2022-12-14 17:35:26'),
(63, 'b3eaf388553dc4aa', '12810', '2022-12-14 14:06:10', NULL, 'AirtelMoney', '+260978981289', '+260971911215', NULL, 'Use NEW short code *115# for Airtel Money. You have withdrawn ZMW 70.00 from 977138536 Jameson Mwenya. Your balance is ZMW 6.84. Txn. ID: CO221214.1405.H51905.', '2022-12-14 20:06:13', '2022-12-14 20:06:13'),
(64, 'b3eaf388553dc4aa', '12813', '2022-12-14 15:00:44', NULL, '878', '+260978981289', '+260971911214', NULL, 'Service is expired', '2022-12-14 21:00:48', '2022-12-14 21:00:48'),
(65, 'b3eaf388553dc4aa', '12815', '2022-12-14 15:01:32', NULL, '878', '+260978981289', '+260971911214', NULL, 'Service is expired', '2022-12-14 21:01:34', '2022-12-14 21:01:34'),
(66, 'a0cc9c5fedc0d9dd', '140', '2022-12-14 15:28:37', NULL, 'MTN', '+260950003776', '+26096060815', NULL, 'Dear Customer, we are experiencing intermittent data connectivity on the network. Update will be shared once normalized. We regret any inconvenience caused.', '2022-12-14 21:28:37', '2022-12-14 21:28:37'),
(67, 'b3eaf388553dc4aa', '12816', '2022-12-14 16:17:25', NULL, 'Airtel', '+260978981289', '+260971911214', NULL, 'Dear Customer, you can now access Siliza by dialing *117# and select option 8 to borrow talk time. Airtel, the smartphone network.', '2022-12-14 22:17:28', '2022-12-14 22:17:28'),
(68, 'a0cc9c5fedc0d9dd', '141', '2022-12-14 18:38:10', NULL, 'MTN', '+260950003776', '+26096060815', NULL, 'Dear Customer, we are experiencing intermittent data connectivity on the network. Update will be shared once normalized. We regret any inconvenience caused.', '2022-12-15 00:38:10', '2022-12-15 00:38:10'),
(69, 'a0cc9c5fedc0d9dd', '142', '2022-12-15 08:28:43', NULL, '402', '+260950003776', '+26096060815', NULL, 'Yello! You have 1 missed calls from +260966220573 on 15-12-2022 08:29.', '2022-12-15 14:28:46', '2022-12-15 14:28:46'),
(70, 'b3eaf388553dc4aa', '12820', '2022-12-15 08:34:15', NULL, 'Airtel', '+260978981289', '+260971911215', NULL, 'Your Allnet daily K10 will expire within 24 hours at 15/12/2022 08:55 . Dial *117# or use Airtel App link https://bit.ly/2keYWN1 to buy a new bundle.', '2022-12-15 14:34:19', '2022-12-15 14:34:19'),
(71, 'a0cc9c5fedc0d9dd', '143', '2022-12-15 08:38:22', NULL, 'MTN', '+260950003776', '+26096060815', NULL, 'Get the latest Nollywood movie by clicking Premiership news by http://www.youtube.com/results?q=nollywood%20movies&sm=1', '2022-12-15 14:38:23', '2022-12-15 14:38:23'),
(72, 'b3eaf388553dc4aa', '12821', '2022-12-15 08:54:09', NULL, 'Soche', '+260978981289', '+260971911215', NULL, 'Dear Customer, You have entered an incorrect PIN.  If you enter the wrong PIN 5 times, your account shall be blocked', '2022-12-15 14:54:11', '2022-12-15 14:54:11'),
(73, 'b3eaf388553dc4aa', '12822', '2022-12-15 08:54:10', NULL, 'AirtelMoney', '+260978981289', '+260971911215', NULL, 'The PIN you have entered is incorrect. Pin should be numeric only and nonnegative.', '2022-12-15 14:55:36', '2022-12-15 14:55:36'),
(74, 'b3eaf388553dc4aa', '12823', '2022-12-15 08:55:04', NULL, 'Soche', '+260978981289', '+260971911215', NULL, 'Use NEW short code *117# to buy Minutes. Thank you for buying K2.0 Pack giving you 9Min, 100SMS . Valid till 16-12-2022 08:55 To check balance dial *117*14#.', '2022-12-15 14:55:36', '2022-12-15 14:55:36'),
(75, 'b3eaf388553dc4aa', '12829', '2022-12-15 11:07:19', NULL, 'AirtelMoney', '+260978981289', '+260971911215', NULL, 'New password non-compliant with password policy, please try to reset again', '2022-12-15 17:07:22', '2022-12-15 17:07:22'),
(76, 'b3eaf388553dc4aa', '12830', '2022-12-15 11:08:37', NULL, 'AirtelMoney', '+260978981289', '+260971911215', NULL, 'Dear Customer, your PIN has been changed successfully. Dial *115# to access Airtel Money services. For Terms and Conditions, click https://bit.ly/Amtnc', '2022-12-15 17:09:16', '2022-12-15 17:09:16'),
(77, 'b3eaf388553dc4aa', '12831', '2022-12-15 11:09:14', NULL, 'AirtelMoney', '+260978981289', '+260971911215', NULL, 'The Pin you have entered is incorrect. Please type your correct four digit Pin. 5 unsuccessful attempts will lock your account. Dial *115# option 6 then option 1 for forgotten PIN', '2022-12-15 17:10:00', '2022-12-15 17:10:00'),
(78, 'b3eaf388553dc4aa', '12833', '2022-12-15 11:18:24', NULL, 'Absa', '+260978981289', '+260971911214', NULL, 'Dear Mwansa, dial *229# to access your Absa accounts anytime on the mobile banking platform. For details, call 5950', '2022-12-15 17:18:27', '2022-12-15 17:18:27'),
(79, 'b3eaf388553dc4aa', '12835', '2022-12-15 12:20:21', NULL, 'Google', '+260978981289', '+918299901900', NULL, 'G-203330 is your Google verification code.', '2022-12-15 18:20:25', '2022-12-15 18:20:25'),
(80, 'b3eaf388553dc4aa', '12836', '2022-12-15 12:22:06', NULL, 'FACEBOOK', '+260978981289', '+918299901900', NULL, '820 693 is your Instagram code. Don\'t share it.', '2022-12-15 18:24:05', '2022-12-15 18:24:05'),
(81, 'b3eaf388553dc4aa', '12837', '2022-12-15 12:24:04', NULL, 'URBAN', '+260978981289', '+260971911214', NULL, '7478 is your OTP. Kindly use it within 2 minutes else it will expire - URBN', '2022-12-15 18:27:07', '2022-12-15 18:27:07'),
(82, 'a0cc9c5fedc0d9dd', '144', '2022-12-15 12:30:02', NULL, 'MTN UNIK', '+260950003776', '+26096060815', NULL, 'Be UniK!  K75 Only get 300 AllNet minutes, 5GB Data , 75 SMS & 1GB Netflix data weekly. Dial *117*4# NOW!', '2022-12-15 18:30:04', '2022-12-15 18:30:04'),
(83, 'b3eaf388553dc4aa', '12839', '2022-12-15 12:30:15', NULL, 'Twitter', '+260978981289', '+918299901900', NULL, 'Your Twitter confirmation code is 412349.', '2022-12-15 18:30:18', '2022-12-15 18:30:18'),
(84, 'b3eaf388553dc4aa', '12840', '2022-12-15 12:33:14', NULL, 'xiaomi', '+260978981289', '+918299901900', NULL, 'Mi Account verification code: 223565. It expires in 5 minutes.', '2022-12-15 18:37:36', '2022-12-15 18:37:36'),
(85, 'b3eaf388553dc4aa', '12842', '2022-12-15 12:39:34', NULL, 'AIRBNB', '+260978981289', '+918299901900', NULL, 'Your Airbnb verification code is: 928820. Don\'t share this code with anyone; our employees will never ask for the code.', '2022-12-15 18:39:37', '2022-12-15 18:39:37'),
(86, 'b3eaf388553dc4aa', '12843', '2022-12-15 12:45:13', NULL, 'CloudOTP', '+260978981289', '+918299901900', NULL, '575903 is your verification code for web.cashbook.in.', '2022-12-15 18:45:17', '2022-12-15 18:45:17'),
(87, 'b3eaf388553dc4aa', '12844', '2022-12-15 12:48:26', NULL, 'URBAN', '+260978981289', '+260971911214', NULL, '8524 is your OTP. Kindly use it within 2 minutes else it will expire - URBN', '2022-12-15 18:48:31', '2022-12-15 18:48:31'),
(88, 'b3eaf388553dc4aa', '12846', '2022-12-15 12:50:33', NULL, 'PAYPAL', '+260978981289', '+918299901900', NULL, 'PayPal: 492827 is your security code. Don\'t share your code.', '2022-12-15 18:50:36', '2022-12-15 18:50:36'),
(89, 'b3eaf388553dc4aa', '12847', '2022-12-15 12:51:35', NULL, 'Huawei', '+260978981289', '+918299901900', NULL, '(979647)Your Huawei Account verify code, it will be expired after 10 minutes.', '2022-12-15 18:53:25', '2022-12-15 18:53:25'),
(90, 'b3eaf388553dc4aa', '12861', '2022-12-15 14:54:04', NULL, 'AirtelMoney', '+260978981289', '+260971911215', NULL, 'Txn. ID : LP221215.1453.H00057. Payment to AMMOBILE Account NA of ZMW 10.00 is successful. Your Airtel Money balance is ZMW 8.85', '2022-12-15 22:54:51', '2022-12-15 22:54:51'),
(91, 'b3eaf388553dc4aa', '12862', '2022-12-15 16:54:48', NULL, 'Airtel Data', '+260978981289', '+260971911214', NULL, 'You have used 60% of one of your Ikali bundles.To check total balance or buy topup bundles Dial *117#,then 4 or Click https://bit.ly/2keYWN1 for AirtelApp', '2022-12-15 23:50:11', '2022-12-15 23:50:11'),
(92, 'b3eaf388553dc4aa', '12868', '2022-12-15 18:18:29', NULL, 'Absa', '+260978981289', '+260971911214', NULL, 'Airtel payment accepted.\nCust Ref 260971591228\nAmt ZMW \nTrans ID 51671121043525\nReference 167453423', '2022-12-16 00:19:19', '2022-12-16 00:19:19'),
(93, 'b3eaf388553dc4aa', '12869', '2022-12-15 18:19:17', NULL, 'Ikali', '+260978981289', '+260971911215', NULL, 'Use NEW short code *117# to buy Ikali. Thank you for choosing Ikali. You have purchased a Daily pack of 1.20GB of Data valid until 16-12-2022 18:19', '2022-12-16 00:19:20', '2022-12-16 00:19:20'),
(94, 'b3eaf388553dc4aa', '12867', '2022-12-15 18:18:28', NULL, 'AirtelMoney', '+260978981289', '+260971911215', NULL, 'Trans. ID :AO221215.1818.J02551. Allocation to your account 971591228 is successful. Transaction amount :ZMW 10.00', '2022-12-16 00:19:25', '2022-12-16 00:19:25'),
(95, 'b3eaf388553dc4aa', '12873', '2022-12-16 07:00:02', NULL, 'Airtel', '+260978981289', '+260971911214', NULL, 'Your Beep call request was successful.', '2022-12-16 13:00:05', '2022-12-16 13:00:05'),
(96, 'a0cc9c5fedc0d9dd', '147', '2022-12-16 09:06:56', NULL, 'MTN', '+260950003776', '+26096060815', NULL, 'JUST FOR YOU! We have internet bundles meant for ONLY YOU! Be it hourly, daily, weekly or monthly. Dial *117# and select NOW!!', '2022-12-16 15:06:59', '2022-12-16 15:06:59'),
(97, 'a0cc9c5fedc0d9dd', '148', '2022-12-16 09:19:22', NULL, 'MoMo', '+260950003776', '+26096060815', NULL, 'Use MoMoPay at tonight\'s Lusaka Night Market at Leopards Hill Mall to pay for all your favourite things! Dial *115# and Select option 5 MoMoPay.', '2022-12-16 15:19:25', '2022-12-16 15:19:25'),
(98, 'b3eaf388553dc4aa', '12878', '2022-12-16 09:34:16', NULL, 'Soche', '+260978981289', '+260971911215', NULL, 'Use NEW short code *117# to buy Minutes. Thank you for buying K2.0 Pack giving you 9Min, 100SMS . Valid till 17-12-2022 09:34 To check balance dial *117*14#.', '2022-12-16 15:34:28', '2022-12-16 15:34:28'),
(99, 'a0cc9c5fedc0d9dd', '152', '2022-12-16 10:54:28', NULL, '+260966220156', '+260950003776', '+26096060815', NULL, 'Musanchi.Namposya@mtn.com', '2022-12-16 16:54:30', '2022-12-16 16:54:30'),
(100, 'a0cc9c5fedc0d9dd', '154', '2022-12-16 11:35:02', NULL, 'ZAMTELMONEY', '+260950003776', '+26095199004', NULL, 'BIG DISCOUNTS on Voice & Data packs every Tuesday on Zamtel Mobile Money! To enjoy this, dial *115#, choose Activate and create a PIN to activate your account.', '2022-12-16 04:05:06', '2022-12-16 04:05:06'),
(101, 'a0cc9c5fedc0d9dd', '155', '2022-12-16 13:09:11', NULL, 'MoMo', '+260950003776', '+26096060815', NULL, 'You have transferred 32.50 ZMW to Moses Mulenga (260964493125) from your mobile money account 62098814 at 2022-12-16 13:09:05. Your new balance: 42.33 ZMW. Message from sender: Hair cut. Message to receiver: Hair cut. Financial Transaction ID: 3623704928.', '2022-12-16 05:39:14', '2022-12-16 05:39:14'),
(102, 'a0cc9c5fedc0d9dd', '156', '2022-12-16 15:41:08', NULL, '+260966220573', '+260950003776', '+26096060815', NULL, 'I\'ll call you back.', '2022-12-16 08:11:10', '2022-12-16 08:11:10'),
(103, 'a0cc9c5fedc0d9dd', '157', '2022-12-17 12:55:25', NULL, 'MoMo', '+260950003776', '+26096060815', NULL, 'You have withdrawn 24.00 ZMW from your mobile money account at  on 2022-12-17 12:55:19. Your new balance:15.83 ZMW. Financial Transaction Id: 3626727550.', '2022-12-17 05:25:28', '2022-12-17 05:25:28'),
(104, 'b3eaf388553dc4aa', '12911', '2022-12-17 21:39:51', NULL, 'AirtelMoney', '+260978981289', '+260971911215', NULL, 'Dear Customer, you have received ZMW 100.00 from 978980800 JOSEPH NAMBOTA. Dial *115# to check your new balance. Txn ID: PP221217.2139.L91246.', '2022-12-17 14:09:54', '2022-12-17 14:09:54'),
(105, 'b3eaf388553dc4aa', '12912', '2022-12-17 22:08:34', NULL, 'AirtelMoney', '+260978981289', '+260971911215', NULL, 'Dear Customer, you have received ZMW 100.00 from 979100106 ANNIE BANDA. Dial *115# to check your new balance. Txn ID: PP221217.2208.L93298.', '2022-12-17 14:38:40', '2022-12-17 14:38:40'),
(106, 'b3eaf388553dc4aa', '12913', '2022-12-17 22:13:37', NULL, '+260979100106', '+260978981289', '+260971911248', NULL, 'I have sent a K100 mudala', '2022-12-17 14:43:46', '2022-12-17 14:43:46'),
(107, 'b3eaf388553dc4aa', '12916', '2022-12-17 23:06:37', NULL, 'AirtelMoney', '+260978981289', '+260971911215', NULL, 'You have entered an invalid PIN length. Please enter correct 4 digit PIN to perform your transaction.', '2022-12-17 15:36:40', '2022-12-17 15:36:40'),
(108, 'b3eaf388553dc4aa', '12918', '2022-12-17 23:16:23', NULL, 'AirtelMoney', '+260978981289', '+260971911215', NULL, 'The Pin you have entered is incorrect. Please type your correct four digit Pin. 5 unsuccessful attempts will lock your account. Dial *115# option 6 then option 1 for forgotten PIN', '2022-12-17 15:46:26', '2022-12-17 15:46:26'),
(109, 'b3eaf388553dc4aa', '12919', '2022-12-17 23:18:03', NULL, 'AirtelMoney', '+260978981289', '+260971911215', NULL, 'Use NEW short code *115# for Airtel Money. Txn. ID : PP221217.2318.I18538. You have sent Money to Judith Nawakwi on 777012664. Amount ZMW 20.00. Your available balance is ZMW 80.67.', '2022-12-17 15:48:06', '2022-12-17 15:48:06'),
(110, 'b3eaf388553dc4aa', '12920', '2022-12-18 07:22:11', NULL, 'Soche', '+260978981289', '+260971911215', NULL, 'Use NEW short code *117# to buy Minutes. Thank you for buying K5.0 Pack giving you 36Min, 250SMS and 20MB. Valid till 19-12-2022 07:22 To check balance dial *117*14#.', '2022-12-17 23:52:15', '2022-12-17 23:52:15'),
(111, 'b3eaf388553dc4aa', '12922', '2022-12-18 07:27:00', NULL, 'AirtelMoney', '+260978981289', '+260971911215', NULL, 'Txn. ID : ES221218.0726.K13357. You currently have ZMW 107.85 available on your account.', '2022-12-17 23:57:02', '2022-12-17 23:57:02'),
(112, 'b3eaf388553dc4aa', '12923', '2022-12-18 07:28:03', NULL, '0974530888', '+260978981289', '+260971911214', NULL, 'Hi, I tried to call you , but could not reach you on 2022-12-18 at 07:27:32. Please call me, Thank you', '2022-12-17 23:58:14', '2022-12-17 23:58:14'),
(113, 'b3eaf388553dc4aa', '12925', '2022-12-18 09:06:06', NULL, 'AirtelMoney', '+260978981289', '+260971911215', NULL, 'Use NEW short code *115# for Airtel Money. You have withdrawn ZMW 60.00 from 770706218 EDDY MALAMBO. Your balance is ZMW 13.17. Txn. ID: CO221218.0905.L08627.', '2022-12-18 01:36:09', '2022-12-18 01:36:09'),
(114, 'b3eaf388553dc4aa', '12926', '2022-12-18 10:03:26', NULL, 'Soche', '+260978981289', '+260971911215', NULL, 'Use NEW short code *117# to buy Minutes. Thank you for buying K2.0 Pack giving you 7Min, 100SMS . Valid till 19-12-2022 10:03 To check balance dial *117*14#.', '2022-12-18 02:33:31', '2022-12-18 02:33:31'),
(115, 'b3eaf388553dc4aa', '12926', '2022-12-18 10:03:26', NULL, 'Soche', '+260978981289', '+260971911215', NULL, 'Use NEW short code *117# to buy Minutes. Thank you for buying K2.0 Pack giving you 7Min, 100SMS . Valid till 19-12-2022 10:03 To check balance dial *117*14#.', '2022-12-18 02:33:31', '2022-12-18 02:33:31'),
(116, 'b3eaf388553dc4aa', '12929', '2022-12-18 11:01:07', NULL, 'Airtel TV', '+260978981289', '+260971911214', NULL, 'Don\'t miss the World Cup final today. Watch Argentina vs France at 17hrs on Airtel TV via ZNBC TV1. Access Airtel app by clicking https://bit.ly/3aOcbuP', '2022-12-18 03:31:09', '2022-12-18 03:31:09'),
(117, 'b3eaf388553dc4aa', '12931', '2022-12-18 16:22:43', NULL, '0974530888', '+260978981289', '+260971911214', NULL, 'Hi, I tried to call you , but could not reach you on 2022-12-18 at 16:22:38. Please call me, Thank you', '2022-12-18 08:52:49', '2022-12-18 08:52:49'),
(118, 'b3eaf388553dc4aa', '12934', '2022-12-18 19:37:33', NULL, 'Airtel Data', '+260978981289', '+260971911214', NULL, 'You have used 60% of one of your Ikali bundles.To check total balance or buy topup bundles Dial *117#,then 4 or Click https://bit.ly/2keYWN1 for AirtelApp', '2022-12-18 12:07:37', '2022-12-18 12:07:37'),
(119, 'b3eaf388553dc4aa', '12936', '2022-12-19 01:02:08', NULL, 'Soche', '+260978981289', '+260971911215', NULL, 'Dear Customer, You have entered an incorrect PIN.  If you enter the wrong PIN 5 times, your account shall be blocked', '2022-12-18 17:32:12', '2022-12-18 17:32:12'),
(120, 'b3eaf388553dc4aa', '12937', '2022-12-19 01:03:12', NULL, 'Soche', '+260978981289', '+260971911215', NULL, 'You do not have enough funds to purchase this pack. Please recharge and try again later.', '2022-12-18 17:33:16', '2022-12-18 17:33:16'),
(121, 'b3eaf388553dc4aa', '12939', '2022-12-19 01:04:08', NULL, 'Soche', '+260978981289', '+260971911215', NULL, 'You do not have enough funds to purchase this pack. Please recharge and try again later.', '2022-12-18 17:34:13', '2022-12-18 17:34:13'),
(122, 'b3eaf388553dc4aa', '12939', '2022-12-19 01:04:08', NULL, 'Soche', '+260978981289', '+260971911215', NULL, 'You do not have enough funds to purchase this pack. Please recharge and try again later.', '2022-12-18 17:34:13', '2022-12-18 17:34:13'),
(123, 'a0cc9c5fedc0d9dd', '160', '2022-12-19 10:15:18', NULL, '+4400', '+260950003776', '+26095199004', NULL, 'ZAMTEL: K121,317 TONIGHT!\n\n0950003776 can win K121,317 with 1 FREE SMS!\nHurry up!\n\nSend WIN to 4400\n\nAfter 1 day: K1/day\nSend WIN', '2022-12-19 02:45:21', '2022-12-19 02:45:21'),
(124, 'b3eaf388553dc4aa', '12951', '2022-12-19 10:35:16', NULL, 'Ikali', '+260978981289', '+260971911215', NULL, 'Dear Customer, you do not have sufficient funds. Please recharge your account to purchase this offer.', '2022-12-19 03:05:20', '2022-12-19 03:05:20'),
(125, 'b3eaf388553dc4aa', '12952', '2022-12-19 10:35:49', NULL, 'Ikali', '+260978981289', '+260971911215', NULL, 'Dear Customer, you do not have sufficient funds. Please recharge your account to purchase this offer.', '2022-12-19 03:05:51', '2022-12-19 03:05:51'),
(126, 'b3eaf388553dc4aa', '12953', '2022-12-19 10:41:36', NULL, '+211', '+260978981289', '+26095199004', NULL, 'Dear Customer, you have successfully activated the 2.5GB§WEEKLY§BUNDLE package.\nA  10.00  Kwacha transaction fee has been deducted from your account successfully.', '2022-12-19 04:30:19', '2022-12-19 04:30:19');

-- --------------------------------------------------------

--
-- Table structure for table `smtp_setting`
--

CREATE TABLE `smtp_setting` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `server` varchar(255) NOT NULL,
  `username` text NOT NULL,
  `password` text NOT NULL,
  `port` int(11) NOT NULL,
  `driver` varchar(255) NOT NULL,
  `encryption` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `smtp_setting`
--

INSERT INTO `smtp_setting` (`id`, `server`, `username`, `password`, `port`, `driver`, `encryption`, `created_at`, `updated_at`) VALUES
(1, 'mail.vibrantcoders.com', 'hr@vibrantcoders.com', 'Vibrant@2020', 587, 'smtp', 'SSL', '2022-11-23 15:20:36', '2022-11-23 15:20:36');

-- --------------------------------------------------------

--
-- Table structure for table `system_setting`
--

CREATE TABLE `system_setting` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `system_name` varchar(255) NOT NULL,
  `website_keywords` varchar(255) NOT NULL,
  `author_name` varchar(255) NOT NULL,
  `date_formate` int(11) NOT NULL,
  `decimal_point` int(11) NOT NULL,
  `footer_text` text NOT NULL,
  `footer_link` text NOT NULL,
  `website_description` text NOT NULL,
  `website_logo` varchar(255) NOT NULL,
  `favicon_icon` varchar(255) NOT NULL,
  `login_logo` varchar(255) DEFAULT NULL,
  `theme_color` varchar(255) DEFAULT NULL,
  `sidebar_color` varchar(255) DEFAULT NULL,
  `sidebar_menu_color` varchar(255) DEFAULT NULL,
  `sidebar_menu_active_color` varchar(255) DEFAULT NULL,
  `login_background_color` varchar(255) DEFAULT NULL,
  `sidebar_navbar_background_color` varchar(255) DEFAULT NULL,
  `sidebar_navbar_font_color` varchar(255) DEFAULT NULL,
  `header_navbar_background_color` varchar(255) DEFAULT NULL,
  `header_navbar_font_color` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `system_setting`
--

INSERT INTO `system_setting` (`id`, `system_name`, `website_keywords`, `author_name`, `date_formate`, `decimal_point`, `footer_text`, `footer_link`, `website_description`, `website_logo`, `favicon_icon`, `login_logo`, `theme_color`, `sidebar_color`, `sidebar_menu_color`, `sidebar_menu_active_color`, `login_background_color`, `sidebar_navbar_background_color`, `sidebar_navbar_font_color`, `header_navbar_background_color`, `header_navbar_font_color`, `created_at`, `updated_at`) VALUES
(1, 'Systemname', '[{\"value\":\"abc\"}]', 'metronic', 1, 2, 'metronic', 'metronic', 'metronic', 'logo-new.png', 'favicon-new.png', NULL, '#f4911e', '#ffffff', '#f4911e', '#e51937', NULL, '#ffffff', '#f4911e', '#ffffff', '#000000', '2022-11-23 15:20:36', '2022-11-23 15:26:58');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `user_no` varchar(255) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `full_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `email_verified_at` timestamp NULL DEFAULT NULL,
  `mobile_no` varchar(255) DEFAULT NULL,
  `password` varchar(255) NOT NULL,
  `designation` varchar(255) DEFAULT NULL,
  `userimage` varchar(255) DEFAULT NULL,
  `user_type` enum('A','U') NOT NULL DEFAULT 'U' COMMENT 'A for Admin, U for Users',
  `status` enum('A','I') NOT NULL DEFAULT 'A' COMMENT 'A for Active, I for not Inactive',
  `is_deleted` enum('Y','N') NOT NULL DEFAULT 'N' COMMENT 'Y for deleted, N for not deleted',
  `remember_token` varchar(100) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `user_no`, `first_name`, `last_name`, `full_name`, `email`, `email_verified_at`, `mobile_no`, `password`, `designation`, `userimage`, `user_type`, `status`, `is_deleted`, `remember_token`, `created_at`, `updated_at`) VALUES
(1, '0', 'Admin', 'Admin', 'Admin Admin', 'admin@demo.com', '2022-11-23 15:20:36', NULL, '$2y$10$dO3bmrmrLV4QGvX6EMXkF.07my3uugJkNns8Ce0uaTlzh/3lPY766', NULL, 'default.png', 'A', 'A', 'N', NULL, '2022-11-23 15:20:36', '2022-11-23 15:20:36'),
(2, '864040', 'GRB', 'Comviva', 'GRB Comviva', 'grb@comviva.com', NULL, NULL, '$2y$10$VGnVhdxyMoivBRELzZdYs.NFvaavW2slx40eNS2I4E9kE9mU//bQG', NULL, 'userimage1669190261.jpg', 'U', 'A', 'N', NULL, '2022-11-23 15:46:06', '2022-11-23 15:58:35');

-- --------------------------------------------------------

--
-- Table structure for table `users_report`
--

CREATE TABLE `users_report` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `user_id` int(11) NOT NULL,
  `response` text NOT NULL,
  `system_no` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `users_report`
--

INSERT INTO `users_report` (`id`, `user_id`, `response`, `system_no`, `created_at`, `updated_at`) VALUES
(1, 1, '{\"Admin\": [{\"Google\": {\"Brand URL\": \"https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin\", \"Mobile Numer\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"Run by\": 1, \"First Name\": \"Randall\", \"Last Name\": \"Romero\", \"User Name\": \"Randall143007uvc\", \"Password\": \"Randall@123\", \"Confirm Password\": \"Randall@123\", \"Message\": \"Failed to generate OTP\"}}]}', '2868723500', '2022-11-29 17:37:40', '2022-11-29 17:37:40'),
(2, 1, '{\"Admin\": [{\"Google\": {\"Brand URL\": \"https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin\", \"Mobile Numer\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"Run by\": 1, \"First Name\": \"Stephen\", \"Last Name\": \"Brown\", \"User Name\": \"Stephen143007uvc\", \"Password\": \"Stephen@123\", \"Confirm Password\": \"Stephen@123\", \"Message\": \"Failed to generate OTP\"}}]}', '2868723500', '2022-11-29 17:41:53', '2022-11-29 17:41:53'),
(3, 1, '{\"Admin\": [{\"Google\": {\"Brand URL\": \"https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin\", \"Mobile Numer\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"Run by\": 1, \"First Name\": \"Collin\", \"Last Name\": \"Allen\", \"User Name\": \"Collin143007uvc\", \"Password\": \"Collin@123\", \"Confirm Password\": \"Collin@123\", \"Message\": \"Failed to generate OTP\"}}]}', '2868723500', '2022-11-29 18:16:02', '2022-11-29 18:16:02'),
(4, 1, '{\"Admin\": [{\"Facebook\": {\"Brand URL\": \"https://www.facebook.com\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"First Name\": \"Adam\", \"Last Name\": \"Hammond\", \"Number\": \"919824345559\", \"Password\": \"Adam@1990\", \"year\": \"1990\", \"message\": \"Failed to generated OTP\"}}]}', '2868723500', '2022-11-30 18:51:53', '2022-11-30 18:51:53'),
(5, 1, '{\"Admin\": [{\"Google\": {\"Brand URL\": \"https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin\", \"Mobile Numer\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"Run by\": 1, \"First Name\": \"Mark\", \"Last Name\": \"Smith\", \"User Name\": \"Mark143007uvc\", \"Password\": \"Mark@123\", \"Confirm Password\": \"Mark@123\", \"Message\": \"Failed to generate OTP\"}}]}', '2868723500', '2022-12-06 18:21:38', '2022-12-06 18:21:38'),
(6, 1, '{\"Admin\": [{\"Google\": {\"Brand URL\": \"https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin\", \"Mobile Numer\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"Run by\": 1, \"First Name\": \"Stuart\", \"Last Name\": \"Brown\", \"User Name\": \"Stuart143007uvc\", \"Password\": \"Stuart@123\", \"Confirm Password\": \"Stuart@123\", \"Message\": \"Failed to generate OTP\"}}]}', '2868723500', '2022-12-06 18:29:48', '2022-12-06 18:29:48'),
(7, 2, '{\"Admin\": [{\"Google\": {\"Brand URL\": \"https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin\", \"Mobile Numer\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"Run by\": 2, \"First Name\": \"Daniel\", \"Last Name\": \"Collins\", \"User Name\": \"Daniel143007uvc\", \"Password\": \"Daniel@123\", \"Confirm Password\": \"Daniel@123\", \"Message\": \"OTP generated successfully\"}}]}', '2868723500', '2022-12-16 06:08:32', '2022-12-16 06:08:32'),
(8, 2, '{\"Admin\": [{\"Facebook\": {\"Brand URL\": \"https://www.facebook.com\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"First Name\": \"George\", \"Last Name\": \"Clark\", \"Number\": \"919824345559\", \"Password\": \"George@1990\", \"year\": \"1990\", \"message\": \"Failed to generated OTP\"}}]}', '2868723500', '2022-12-16 06:17:25', '2022-12-16 06:17:25'),
(9, 2, '{\"Admin\": [{\"InstagramWeb\": {\"Brand URL\": \"https://www.instagram.com/accounts/emailsignup/?hl=en\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"First Name\": \"Joshua\", \"Last Name\": \"Wilson\", \"Number\": \"919824345559\", \"Password\": \"Joshua@1990\", \"year\": 1967, \"Message\": \"OTP generated successfully\"}}]}', '2868723500', '2022-12-16 06:20:02', '2022-12-16 06:20:02'),
(10, 2, '{\"Admin\": [{\"Twitter\": {\"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"First Name\": \"Timothy\", \"Number\": \"+919824345559\", \"Year\": 1997, \"Message\": \"Failed to generated OTP\"}}]}', '2868723500', '2022-12-16 06:22:26', '2022-12-16 06:22:26'),
(11, 2, '{\"Admin\": [{}]}', '2868723500', '2022-12-16 06:24:01', '2022-12-16 06:24:01'),
(12, 2, '{\"Admin\": [{\"Skype\": {\"Brand URL\": \"https://signup.live.com/signup?lcid=1033&wa=wsignin1.0&rpsnv=13&ct=1661151965&rver=7.1.6819.0&wp=MBI_SSL&wreply=https%3a%2f%2flw.skype.com%2flogin%2foauth%2fproxy%3fclient_id%3d578134%26redirect_uri%3dhttps%253A%252F%252Fweb.skype.com%26source%3dscomnav%2\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"First Name\": \"Brian\", \"Last Name\": \"Gray\", \"Number\": \"919824345559\", \"Password\": \"Brian@1990\", \"Message\": \"Failed to generated OTP\"}}]}', '2868723500', '2022-12-16 06:25:20', '2022-12-16 06:25:20'),
(13, 2, '{\"Admin\": [{}]}', '2868723500', '2022-12-16 06:27:03', '2022-12-16 06:27:03'),
(14, 2, '{\"Admin\": [{}]}', '2868723500', '2022-12-16 06:28:28', '2022-12-16 06:28:28'),
(15, 2, '{\"Admin\": [{\"Linkedin\": {\"Brand URL\": \"https://www.linkedin.com/reg/join\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"First Name\": \"Kyle\", \"Last Name\": \"Gonzalez\", \"Number\": \"+919824345559\", \"Password\": \"Kyle@1990\", \"Message\": \"Failed to generated OTP\"}}]}', '2868723500', '2022-12-16 06:31:33', '2022-12-16 06:31:33'),
(16, 2, '{\"Admin\": [{\"Yahoo\": {\"Brand URL\": \"https://login.yahoo.com/account/create?.lang=en-IN&.intl=in&.src=yhelp\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"First Name\": \"Matthew\", \"Last Name\": \"Ramos\", \"Number\": \"919824345559\", \"Password\": \"yahooo@1990\", \"year\": 1987, \"message\": \"Failed to generated OTP\"}}]}', '2868723500', '2022-12-16 06:33:58', '2022-12-16 06:33:58'),
(17, 2, '{\"Admin\": [{\"Amazon\": {\"Brand URL\": \"https://www.amazon.com\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"First Name\": \"Christopher\", \"Email\": 9824345559, \"Password\": \"Christopher@1990\", \"Message\": \"Failed to generate OTP\"}}]}', '2868723500', '2022-12-16 06:38:25', '2022-12-16 06:38:25'),
(18, 2, '{\"Admin\": [{\"Microsoftteam\": {\"Brand URL\": \"https://signup.live.com/signup?sru=https%3a%2f%2flogin.live.com%2foauth20_authorize.srf%3flc%3d1033%26mkt%3dEN-US%26opid%3dE1C4FAD9D6AF98B4%26opidt%3d1662450211%26uaid%3df7e93e1baf48418bbb681ceb04a62c04%26opignore%3d1&mkt=EN-US&uiflavor=web&lw=1&fl=easi2&\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"Number\": \"919824345559\", \"Password\": \"Daniel@1990\", \"message\": \"Failed to generated OTP\"}}]}', '2868723500', '2022-12-16 06:41:56', '2022-12-16 06:41:56'),
(19, 2, '{\"Admin\": [{\"Badoo\": {\"Brand URL\": \"https://badoo.com/signup/\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"Number\": \"+919824345559\", \"Password\": \"ScottJones\", \"Message\": \"Failed to generate OTP\"}}]}', '2868723500', '2022-12-16 06:42:51', '2022-12-16 06:42:51'),
(20, 2, '{\"Admin\": [{\"DingWeb\": {\"Brand URL\": \"https://www.ding.com/register\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"Number\": \"+919824345559\", \"Message\": \"OTP generated successfully\"}}]}', '2868723500', '2022-12-16 06:44:40', '2022-12-16 06:44:40'),
(21, 2, '{\"Admin\": [{\"Airbnb\": {\"Brand URL\": \"https://www.airbnb.co.in/\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"Number\": \"919824345559\", \"Message\": \"Failed to generated OTP\"}}]}', '2868723500', '2022-12-16 06:47:10', '2022-12-16 06:47:10'),
(22, 2, '{\"Admin\": [{}]}', '2868723500', '2022-12-16 06:55:20', '2022-12-16 06:55:20'),
(23, 2, '{\"Admin\": [{\"Uber\": {\"Brand URL\": \"drivers.uber.com\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"Number\": \"+919824345559\", \"Message\": \"Failed to generate OTP\"}}]}', '2868723500', '2022-12-16 06:56:43', '2022-12-16 06:56:43'),
(24, 2, '{\"Admin\": [{\"Uber\": {\"Brand URL\": \"drivers.uber.com\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"Number\": \"+919824345559\", \"Message\": \"Failed to generate OTP\"}}]}', '2868723500', '2022-12-16 06:58:21', '2022-12-16 06:58:21'),
(25, 2, '{\"Admin\": [{\"Facebook\": {\"Brand URL\": \"https://www.facebook.com\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"First Name\": \"Alex\", \"Last Name\": \"Mcdonald\", \"Number\": \"919824345559\", \"Password\": \"Alex@1990\", \"year\": \"1990\", \"message\": \"Failed to generated OTP\"}, \"Google\": {\"Brand URL\": \"https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin\", \"Mobile Numer\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"Run by\": 2, \"First Name\": \"Matthew\", \"Last Name\": \"Mcgee\", \"User Name\": \"Matthew143007uvc\", \"Password\": \"Matthew@123\", \"Confirm Password\": \"Matthew@123\", \"Message\": \"OTP generated successfully\"}, \"InstagramWeb\": {\"Brand URL\": \"https://www.instagram.com/accounts/emailsignup/?hl=en\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"First Name\": \"Adrian\", \"Last Name\": \"Rodriguez\", \"Number\": \"919824345559\", \"Password\": \"Adrian@1990\", \"year\": 1991, \"Message\": \"OTP generated successfully\"}, \"Twitter\": {\"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"First Name\": \"Glen\", \"Number\": \"+919824345559\", \"Year\": 1961, \"Message\": \"Failed to generated OTP\"}, \"Skype\": {\"Brand URL\": \"https://signup.live.com/signup?lcid=1033&wa=wsignin1.0&rpsnv=13&ct=1661151965&rver=7.1.6819.0&wp=MBI_SSL&wreply=https%3a%2f%2flw.skype.com%2flogin%2foauth%2fproxy%3fclient_id%3d578134%26redirect_uri%3dhttps%253A%252F%252Fweb.skype.com%26source%3dscomnav%2\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"First Name\": \"Anthony\", \"Last Name\": \"Mayer\", \"Number\": \"919824345559\", \"Password\": \"Anthony@1990\", \"Message\": \"Failed to generated OTP\"}, \"Uber\": {\"Brand URL\": \"drivers.uber.com\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"Number\": \"+919824345559\", \"Message\": \"Failed to generate OTP\"}, \"Linkedin\": {\"Brand URL\": \"https://www.linkedin.com/reg/join\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"First Name\": \"Charles\", \"Last Name\": \"Walker\", \"Number\": \"+919824345559\", \"Password\": \"Charles@1990\", \"Message\": \"Failed to generated OTP\"}, \"Yahoo\": {\"Brand URL\": \"https://login.yahoo.com/account/create?.lang=en-IN&.intl=in&.src=yhelp\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"First Name\": \"Jonathan\", \"Last Name\": \"Green\", \"Number\": \"919824345559\", \"Password\": \"yahooo@1990\", \"year\": 1977, \"message\": \"Failed to generated OTP\"}, \"Amazon\": {\"Brand URL\": \"https://www.amazon.com\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"First Name\": \"Michael\", \"Email\": 9824345559, \"Password\": \"Michael@1990\", \"Message\": \"Failed to generate OTP\"}, \"Microsoftteam\": {\"Brand URL\": \"https://signup.live.com/signup?sru=https%3a%2f%2flogin.live.com%2foauth20_authorize.srf%3flc%3d1033%26mkt%3dEN-US%26opid%3dE1C4FAD9D6AF98B4%26opidt%3d1662450211%26uaid%3df7e93e1baf48418bbb681ceb04a62c04%26opignore%3d1&mkt=EN-US&uiflavor=web&lw=1&fl=easi2&\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"Number\": \"919824345559\", \"Password\": \"Alejandro@1990\", \"message\": \"Failed to generated OTP\"}, \"Badoo\": {\"Brand URL\": \"https://badoo.com/signup/\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"Number\": \"+919824345559\", \"Password\": \"RayRoberts\", \"Message\": \"Failed to generate OTP\"}, \"DingWeb\": {\"Brand URL\": \"https://www.ding.com/register\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"Number\": \"+919824345559\", \"Message\": \"OTP generated successfully\"}, \"Airbnb\": {\"Brand URL\": \"https://www.airbnb.co.in/\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"Number\": \"919824345559\", \"Message\": \"Failed to generated OTP\"}}]}', '2868723500', '2022-12-16 07:18:59', '2022-12-16 07:18:59'),
(26, 2, '{\"Admin\": [{\"Twitter\": {\"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"First Name\": \"James\", \"Number\": \"+919824345559\", \"Year\": 1978, \"Message\": \"Failed to generated OTP\"}}]}', '2868723500', '2022-12-16 07:46:18', '2022-12-16 07:46:18'),
(27, 2, '{\"Admin\": [{\"Twitter\": {\"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"First Name\": \"Steven\", \"Number\": \"+919824345559\", \"Year\": 1993, \"Message\": \"Failed to generated OTP\"}}]}', '2868723500', '2022-12-16 07:50:13', '2022-12-16 07:50:13'),
(28, 2, '{\"Admin\": [{\"Twitter\": {\"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"First Name\": \"Casey\", \"Number\": \"+919824345559\", \"Year\": 1987, \"Message\": \"Failed to generated OTP\"}}]}', '2868723500', '2022-12-16 07:59:50', '2022-12-16 07:59:50'),
(29, 2, '{\"Admin\": [{\"Skype\": {\"Brand URL\": \"https://signup.live.com/signup?lcid=1033&wa=wsignin1.0&rpsnv=13&ct=1661151965&rver=7.1.6819.0&wp=MBI_SSL&wreply=https%3a%2f%2flw.skype.com%2flogin%2foauth%2fproxy%3fclient_id%3d578134%26redirect_uri%3dhttps%253A%252F%252Fweb.skype.com%26source%3dscomnav%2\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"First Name\": \"Michael\", \"Last Name\": \"Mccullough\", \"Number\": \"919824345559\", \"Password\": \"Michael@1990\", \"Message\": \"Failed to generated OTP\"}}]}', '2868723500', '2022-12-16 08:55:26', '2022-12-16 08:55:26'),
(30, 2, '{\"Admin\": [{\"Uber\": {\"Brand URL\": \"https://auth.uber.com/v2/?breeze_local_zone=phx3&next_url=https%3A%2F%2Fdrivers.uber.com%2F&state=vpIRY6JWRP7gqQ0cA8e7JBcHwLBhgmH66jumyuUHcqg%3D\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"Number\": \"+919824345559\", \"Message\": \"OTP generated successfully\"}}]}', '2868723500', '2022-12-16 09:44:45', '2022-12-16 09:44:45'),
(31, 2, '{\"Admin\": [{\"Badoo\": {\"Brand URL\": \"https://badoo.com/signup/\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"Number\": \"+919824345559\", \"Password\": \"DanielTaylor\", \"Message\": \"Failed to generate OTP\"}}]}', '2868723500', '2022-12-16 09:49:26', '2022-12-16 09:49:26'),
(32, 2, '{\"Admin\": [{\"Badoo\": {\"Brand URL\": \"https://badoo.com/signup/\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"Number\": \"+919824345559\", \"Password\": \"BernardSmith\", \"Message\": \"Failed to generate OTP\"}}]}', '2868723500', '2022-12-16 10:00:55', '2022-12-16 10:00:55'),
(33, 2, '{\"Admin\": [{\"Airbnb\": {\"Brand URL\": \"https://www.airbnb.co.in/\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"Number\": \"919824345559\", \"Message\": \"Failed to generated OTP\"}}]}', '2868723500', '2022-12-16 10:05:16', '2022-12-16 10:05:16'),
(34, 2, '{\"Admin\": [{\"Airbnb\": {\"Brand URL\": \"https://www.airbnb.co.in/\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"Number\": \"919824345559\", \"Message\": \"Failed to generated OTP\"}}]}', '2868723500', '2022-12-16 10:08:27', '2022-12-16 10:08:27'),
(35, 2, '{\"Admin\": [{\"Airbnb\": {\"Brand URL\": \"https://www.airbnb.co.in/\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"Number\": \"919824345559\", \"Message\": \"Failed to generated OTP\"}}]}', '2868723500', '2022-12-16 10:11:55', '2022-12-16 10:11:55'),
(36, 2, '{\"Admin\": [{\"Airbnb\": {\"Brand URL\": \"https://www.airbnb.co.in/\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"Number\": \"919824345559\", \"Message\": \"Failed to generated OTP\"}}]}', '2868723500', '2022-12-16 10:14:42', '2022-12-16 10:14:42'),
(37, 2, '{\"Admin\": [{\"Airbnb\": {\"Brand URL\": \"https://www.airbnb.co.in/\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"Number\": \"919824345559\", \"Message\": \"Failed to generated OTP\"}}]}', '2868723500', '2022-12-16 10:17:35', '2022-12-16 10:17:35'),
(38, 2, '{\"Admin\": [{\"Airbnb\": {\"Brand URL\": \"https://www.airbnb.co.in/\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"Number\": \"919824345559\", \"Message\": \"Failed to generated OTP\"}}]}', '2868723500', '2022-12-16 10:19:46', '2022-12-16 10:19:46'),
(39, 2, '{\"Admin\": [{\"Airbnb\": {\"Brand URL\": \"https://www.airbnb.co.in/\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"Number\": \"919824345559\", \"Message\": \"Failed to generated OTP\"}}]}', '2868723500', '2022-12-16 10:21:22', '2022-12-16 10:21:22'),
(40, 2, '{\"Admin\": [{\"Airbnb\": {\"Brand URL\": \"https://www.airbnb.co.in/\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"Number\": \"919824345559\", \"Message\": \"Failed to generated OTP\"}}]}', '2868723500', '2022-12-19 03:02:08', '2022-12-19 03:02:08'),
(41, 2, '{\"Admin\": [{\"Airbnb\": {\"Brand URL\": \"https://www.airbnb.co.in/\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"Number\": \"919824345559\", \"Message\": \"Failed to generated OTP\"}}]}', '2868723500', '2022-12-19 03:04:52', '2022-12-19 03:04:52'),
(42, 2, '{\"Admin\": [{\"Badoo\": {\"Brand URL\": \"https://badoo.com/signup/\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"Number\": \"+919824345559\", \"Password\": \"RyanSalazar\", \"Message\": \"Failed to generate OTP\"}}]}', '2868723500', '2022-12-19 03:11:38', '2022-12-19 03:11:38'),
(43, 2, '{\"Admin\": [{\"Airbnb\": {\"Brand URL\": \"https://www.airbnb.co.in/\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"Number\": \"919824345559\", \"Message\": \"Failed to generated OTP\"}}]}', '2868723500', '2022-12-19 03:17:39', '2022-12-19 03:17:39'),
(44, 2, '{\"Admin\": [{\"Airbnb\": {\"Brand URL\": \"https://www.airbnb.co.in/\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"Number\": \"919824345559\", \"Message\": \"OTP generated successfully\"}}]}', '2868723500', '2022-12-19 03:19:00', '2022-12-19 03:19:00'),
(45, 2, '{\"Admin\": [{\"Yahoo\": {\"Brand URL\": \"https://login.yahoo.com/account/create?.lang=en-IN&.intl=in&.src=yhelp\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"First Name\": \"Alan\", \"Last Name\": \"Benson\", \"Number\": \"919824345559\", \"Password\": \"yahooo@1990\", \"year\": 1987, \"message\": \"Failed to generated OTP\"}}]}', '2868723500', '2022-12-19 03:44:26', '2022-12-19 03:44:26'),
(46, 2, '{\"Admin\": [{\"Yahoo\": {\"Brand URL\": \"https://login.yahoo.com/account/create?.lang=en-IN&.intl=in&.src=yhelp\", \"Mobile Number\": 9824345559, \"Device Name\": \"samsung\", \"Device Id\": 1, \"First Name\": \"Michael\", \"Last Name\": \"Jackson\", \"Number\": \"919824345559\", \"Password\": \"yahooo@1990\", \"year\": 1966, \"message\": \"Failed to generated OTP\"}}]}', '2868723500', '2022-12-19 03:51:34', '2022-12-19 03:51:34');

-- --------------------------------------------------------

--
-- Table structure for table `user_type`
--

CREATE TABLE `user_type` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `user_role` varchar(255) NOT NULL,
  `status` int(11) NOT NULL,
  `is_deleted` enum('Y','N') NOT NULL DEFAULT 'N' COMMENT 'Y for deleted, N for not deleted',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `user_type`
--

INSERT INTO `user_type` (`id`, `user_role`, `status`, `is_deleted`, `created_at`, `updated_at`) VALUES
(1, 'Super Admin', 1, 'N', '2022-11-23 15:20:36', '2022-11-23 15:20:36');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `audit_trails`
--
ALTER TABLE `audit_trails`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `brand_entry`
--
ALTER TABLE `brand_entry`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `code_number`
--
ALTER TABLE `code_number`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `countries`
--
ALTER TABLE `countries`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `device`
--
ALTER TABLE `device`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `migrations`
--
ALTER TABLE `migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `mobile_number`
--
ALTER TABLE `mobile_number`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `personal_access_tokens`
--
ALTER TABLE `personal_access_tokens`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `personal_access_tokens_token_unique` (`token`),
  ADD KEY `personal_access_tokens_tokenable_type_tokenable_id_index` (`tokenable_type`,`tokenable_id`);

--
-- Indexes for table `result_reports`
--
ALTER TABLE `result_reports`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `smtp_setting`
--
ALTER TABLE `smtp_setting`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `system_setting`
--
ALTER TABLE `system_setting`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_email_unique` (`email`);

--
-- Indexes for table `users_report`
--
ALTER TABLE `users_report`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_type`
--
ALTER TABLE `user_type`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `audit_trails`
--
ALTER TABLE `audit_trails`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;

--
-- AUTO_INCREMENT for table `brand_entry`
--
ALTER TABLE `brand_entry`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT for table `code_number`
--
ALTER TABLE `code_number`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `countries`
--
ALTER TABLE `countries`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=247;

--
-- AUTO_INCREMENT for table `device`
--
ALTER TABLE `device`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `migrations`
--
ALTER TABLE `migrations`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `mobile_number`
--
ALTER TABLE `mobile_number`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `personal_access_tokens`
--
ALTER TABLE `personal_access_tokens`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `result_reports`
--
ALTER TABLE `result_reports`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=127;

--
-- AUTO_INCREMENT for table `smtp_setting`
--
ALTER TABLE `smtp_setting`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `system_setting`
--
ALTER TABLE `system_setting`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `users_report`
--
ALTER TABLE `users_report`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;

--
-- AUTO_INCREMENT for table `user_type`
--
ALTER TABLE `user_type`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
