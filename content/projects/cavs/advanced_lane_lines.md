---
title: "Advanced Lane Lines Detection"
date: 2019-01-13T21:34:33-05:00
draft: false
---

In this project, the goal is to write a software pipeline to identify the lane boundaries in a video.  <!--more-->

### The steps of this project are the following:

* Compute the camera calibration matrix and distortion coefficients given a set of chessboard images.
* Apply a distortion correction to raw images.
* Use color transforms, gradients, etc., to create a thresholded binary image.
* Apply a perspective transform to rectify binary image ("birds-eye view").
* Detect lane pixels and fit to find the lane boundary.
* Determine the curvature of the lane and vehicle position with respect to center.
* Warp the detected lane boundaries back onto the original image.
* Output visual display of the lane boundaries and numerical estimation of lane curvature and vehicle position.

__[Project on GitHub](https://github.com/amintahmasbi/CarND-Advanced-Lane-Lines)__
