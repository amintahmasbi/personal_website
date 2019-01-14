---
title: "Vehicle Detection"
date: 2019-01-13T21:38:31-05:00
draft: false
---

In this project, the goal is to write a software pipeline to detect vehicles in a video. <!--more-->

### The steps of this project are the following:

* Perform a Histogram of Oriented Gradients (HOG) feature extraction on a labeled training set of images and train a classifier Linear SVM classifier
* Apply a color transform and append binned color features, as well as histograms of color, to your HOG feature vector.
* Normalize features and randomize a selection for training and testing.
* Implement a sliding-window technique and use trained classifier to search for vehicles in images.
* Run pipeline on a video stream and create a heat map of recurring detections frame by frame to reject outliers and follow detected vehicles.
* Estimate a bounding box for vehicles detected.

__[Project on GitHub](https://github.com/amintahmasbi/CarND-Vehicle-Detection)__
