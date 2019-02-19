-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 18, 2019 at 02:50 PM
-- Server version: 10.1.30-MariaDB
-- PHP Version: 7.2.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `comserach`
--

-- --------------------------------------------------------

--
-- Table structure for table `tab1`
--

CREATE TABLE `tab1` (
  `id` int(11) NOT NULL,
  `name` varchar(40) NOT NULL,
  `nickname` varchar(15) NOT NULL,
  `phone` int(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tab1`
--

INSERT INTO `tab1` (`id`, `name`, `nickname`, `phone`) VALUES
(3, 'himanshu kumar', 'himan', 999999999),
(8, 'himanshu kumar', 'himan', 2147483647),
(9, 'mohit babu', 'mohit', 2147483647),
(10, 'vaibhav jaiswal', 'vaibhav', 2147483647),
(11, 'abhinav bijarnia', 'abhi', 2147483647),
(12, 'summit ron', 'summit', 2147483647),
(13, 'dinabandu behara', 'bhera', 2147483647),
(14, 'ashu mohan', 'ashu', 2147483647),
(15, 'vibhanshu yadav', 'yadav', 2147483647),
(16, 'tarun kumar', 'tarun', 2147483647),
(17, 'pragathi sristi', 'pragathi', 2147483647);

-- --------------------------------------------------------

--
-- Table structure for table `tab2`
--

CREATE TABLE `tab2` (
  `id` int(11) NOT NULL,
  `payment` int(15) NOT NULL,
  `date` date NOT NULL,
  `1id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tab2`
--

INSERT INTO `tab2` (`id`, `payment`, `date`, `1id`) VALUES
(1, 50000, '2019-02-19', 3),
(2, 50000, '2019-02-19', 8),
(3, 50000, '2019-02-19', 9),
(4, 50000, '2019-02-19', 10),
(5, 50000, '2019-02-19', 11),
(6, 50000, '2019-02-19', 12),
(7, 50000, '2019-02-19', 13),
(8, 50000, '2019-02-19', 14),
(9, 50000, '2019-02-19', 15),
(10, 50000, '2019-02-19', 16),
(11, 50000, '2019-02-19', 17);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tab1`
--
ALTER TABLE `tab1`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tab2`
--
ALTER TABLE `tab2`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tab1`
--
ALTER TABLE `tab1`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `tab2`
--
ALTER TABLE `tab2`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
