#!/usr/bin/env python
# coding: utf-8

# Reference:
# Omer Sakarya - Selenium Tutorial: Scraping Glassdoor.com in 10 Minutes

from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd


def get_jobs(keyword, num_jobs, verbose, path, slp_time):
    
    '''Gathers jobs as a dataframe, scraped from Glassdoor'''
    
    #Initializing the webdriver
    options = webdriver.ChromeOptions()
    
    #Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    #options.add_argument('headless')
    #ChromeOptions options = new ChromeOptions();
    #options.addArguments("--incognito");
    #DesiredCapabilities capabilities = DesiredCapabilities.chrome();
    #capabilities.setCapability(ChromeOptions.CAPABILITY, options);
    
    #Change the path to where chromedriver is in your home folder.
    driver = webdriver.Chrome(executable_path=path, options=options)
    driver.set_window_size(1120, 1000)

    #San Fransico, CA
    #url_CA = 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword=' + keyword + '&locT=C&locId=1147401&locKeyword=San%20Fransico,%20CA&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=100&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0'
    
    #San Jose, CA
    #url = 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword=' + keyword + '&locT=C&locId=1147436&locKeyword=San%20Jose,%20CA&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=50&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0'
    
    #San Antonio, TX
    #url_TX = 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword=' + keyword + '&locT=C&locId=1140494&locKeyword=San%20Antonio,%20TX&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=100&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0'
    
    #Saint Louis, MO
    #url_MO = 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword=' + keyword + '&locT=C&locId=1131270&locKeyword=Saint%20Louis,%20MO&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=50&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0'
    
    #Boulder, CO
    #url_CO = 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword=' + keyword + '&locT=C&locId=1131270&locKeyword=Saint%20Louis,%20MO&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=50&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0'
        
    #any where in the country
    #url_all  = 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword=' + keyword + '&locT=C&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0'
    
    #Texas
    #url_tx = 'https://www.glassdoor.com/Job/texas-us-data-science-jobs-SRCH_IL.0,8_IS1347_KO9,21.htm?clickSource=searchBox'
        
    #Colorado
    #url_CO = 'https://www.glassdoor.com/Job/colorado-us-data-science-jobs-SRCH_IL.0,11_IS2519_KO12,24.htm?clickSource=searchBox'
    
    #Missouri
    #url_mo = 'https://www.glassdoor.com/Job/missouri-us-data-science-jobs-SRCH_IL.0,11_IS386_KO12,24.htm?clickSource=searchBox'
    
    #California
    #url_ca = 'https://www.glassdoor.com/Job/california-us-data-science-jobs-SRCH_IL.0,13_IS2280_KO14,26.htm?clickSource=searchBox'
    
    #Georgia
    #url_ga = 'https://www.glassdoor.com/Job/georgia-us-data-science-jobs-SRCH_IL.0,10_IS3426_KO11,23.htm?clickSource=searchBox'
    
    #Washington
    #url_wa 'https://www.glassdoor.com/Job/washington-state-us-data-science-jobs-SRCH_IL.0,19_IS3020_KO20,32.htm?clickSource=searchBox'
    
    #United states
    #url_all = 'https://www.glassdoor.com/Job/united-states-data-science-jobs-SRCH_IL.0,13_IN1_KO14,26.htm?clickSource=searchBox'
    
    #any where in the country
    url_all  = 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword=' + keyword + '&locT=C&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0'
    
    
    #url_list = [url_all, url_tx, url_CO, url_MO, url_CA]
    url_list = [url_all]
    jobs = []
    
    for url in url_list:
    
        driver.get(url)

        while len(jobs) < num_jobs:  #If true, should be still looking for new jobs.

            #Let the page load. Change this number based on your internet speed.
            #Or, wait until the webpage is loaded, instead of hardcoding it.
            time.sleep(slp_time)

            #Test for the "Sign Up" prompt and get rid of it.
            try:
                #driver.find_element_by_class_name("selected").click()
                driver.find_element_by_xpath('//*[@id="MainCol"]/div[1]/ul/li[1]').click()
                print("selected first job posting")
            except ElementClickInterceptedException:
                print("failed first job posting")
                pass

            time.sleep(.1)

            try:
                #Line from the orignial code did not work
                #driver.find_element_by_class_name("ModalStyle__xBtn___29PT9").click()  #clicking to the X.

                driver.find_element_by_css_selector('[alt="Close"]').click()
            except NoSuchElementException:
                pass

            #Origninal Code - Going through each job in this page
            #jl for Job Listing. These are the buttons we're going to click.
            #job_buttons = driver.find_elements_by_class_name("jl")


            # xpath: 
            # //*[@id="MainCol"]/div[1]/ul/li[1]
            # //*[@id="MainCol"]/div[1]/ul/li[2]
            # //*[@id="MainCol"]/div[1]/ul/li[1]

            job_buttons = []
            job_count = 0
            #My code - create for loop to create job_buttons array:
            for i in range(1, 36):
                job_buttons.append('//*[@id="MainCol"]/div[1]/ul/li[' + str(i) + ']')

            #Troubleshooting
            #for job_button in job_buttons:
                #driver.find_element_by_xpath(job_button).click()  #You might
                #job_button.click()
                #time.sleep(5)


            #print(job_buttons)
            for job_button in job_buttons:  
                job_count += 1
                #print(job_count)
                
                if job_count <= 28:
                    try:
                        driver.find_element_by_xpath(job_button).click()
                        time.sleep(5)
                        collected_successfully = False
                    except NoSuchElementException:
                        print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
                        break
                else:
                    #driver.find_element_by_xpath('.//li[@class="next"]//a').click()
                    #xpath: //*[@id="MainCol"]/div[2]/div/div[1]/button[7]
                    job_count = 0
                    driver.find_element_by_xpath('//*[@id="MainCol"]/div[2]/div/div[1]/button[7]').click()
                    time.sleep(5)
                    break

                        
                print("Progress: {}".format("" + str(len(jobs)) + "/" + str(num_jobs)))
                if len(jobs) >= num_jobs:
                    break

                #job_button.click
                #try:
                    #driver.find_element_by_xpath(job_button).click()  #You might 
                    #time.sleep(5)
                    #collected_successfully = False
                #except NoSuchElementException:
                    #driver.find_element_by_xpath('.//li[@class="next"]//a').click()
                    #xpath: //*[@id="MainCol"]/div[2]/div/div[1]/button[7]
                    #driver.find_element_by_xpath('//*[@id="MainCol"]/div[2]/div/div[1]/button[5]').click()
                    #collected_successfully = False

                print("In job buttons loop")

                while not collected_successfully:
                    try:
                        #Origninal Code
                        #company_name = driver.find_element_by_xpath('.//div[@class="employerName"]').text
                        #location = driver.find_element_by_xpath('.//div[@class="location"]').text
                        #job_title = driver.find_element_by_xpath('.//div[contains(@class, "title")]').text
                        #job_description = driver.find_element_by_xpath('.//div[@class="jobDescriptionContent desc"]').text


                        company_name = driver.find_element_by_xpath("//div[@class='css-xuk5ye e1tk4kwz5']").text
                        location = driver.find_element_by_xpath("//div[@class='css-56kyx5 e1tk4kwz1']").text
                        job_title = driver.find_element_by_xpath("//div[@class='css-1j389vi e1tk4kwz2']").text
                        job_description = "Data Science"
                        collected_successfully = True
                        #print("Company: " + company_name + ", location: " + location + ", Title: " + job_title + ", desc: " + job_description)
                    except:
                        try:
                            #xpath try button: //*[@id="JDCol"]/div/div[2]/button
                            driver.find_element_by_xpath('//*[@id="JDCol"]/div/div[2]/button').click()
                            time.sleep(5)
                        except:
                            print("while collected loop failed")
                            time.sleep(5)

    #Salary Estimate                    
                try:
                    #salary_estimate = driver.find_element_by_xpath('.//span[@class="gray small salary"]').text
                    salary_estimate = driver.find_element_by_xpath("//span[@class='css-1hbqxax e1wijj240']").text
                    #print(salary_estimate)
                except NoSuchElementException:
                    salary_estimate = -1 #You need to set a "not found value. It's important."

    #Rating                
                try:
                    #rating = driver.find_element_by_xpath('.//span[@class="rating"]').text
                    rating = driver.find_element_by_xpath("//span[@class='css-1m5m32b e1tk4kwz4']").text
                except NoSuchElementException:
                    rating = -1 #You need to set a "not found value. It's important."

                #Printing for debugging
                if verbose:
                    print("Job Title: {}".format(job_title))
                    print("Salary Estimate: {}".format(salary_estimate))
                    print("Job Description: {}".format(job_description[:500]))
                    print("Rating: {}".format(rating))
                    print("Company Name: {}".format(company_name))
                    print("Location: {}".format(location))

                #Going to the Company tab...
                #clicking on this:
                #<div class="tab" data-tab-type="overview"><span>Company</span></div>
                try:
                    #xpath: //*[@id="SerpFixedHeader"]/div/div/div[2]
                    #driver.find_element_by_xpath('.//div[@class="tab" and @data-tab-type="overview"]').click()
                    #driver.find_element_by_xpath('.//div[@class="css-1ap6ha9 ef7s0la0" and @data-tab-type="overview"]').click()
                    driver.find_element_by_xpath('//*[@id="SerpFixedHeader"]/div/div/div[2]').click()

    #Headquarters
                    try:
                        #<div class="infoEntity">
                        #    <label>Headquarters</label>
                        #    <span class="value">San Francisco, CA</span>
                        #</div>
                        #headquarters = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Headquarters"]//following-sibling::*').text

                        #<div class="d-flex flex-wrap">
                        #  <div ...
                        #     <span class="css-1pldt9b e1pvx6aw1">Headquarters</span>
                        #     <span class="....">San Francisco, CA</span>
                        #</div>
                        headquarters = driver.find_element_by_xpath('//span[@class="css-1pldt9b e1pvx6aw1" and text()="Headquarters"]//following-sibling::*').text
                    except NoSuchElementException:
                        headquarters = -1

    #Size
                    try:
                        #size = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Size"]//following-sibling::*').text
                        size = driver.find_element_by_xpath('//span[@class="css-1pldt9b e1pvx6aw1" and text()="Size"]//following-sibling::*').text
                    except NoSuchElementException:
                        size = -1

    #Founded                    
                    try:
                        #founded = driver.find_element_by_xpath('//span[@class="css-1pldt9b e1pvx6aw1"]//label[text()="Founded"]//following-sibling::*').text
                        founded = driver.find_element_by_xpath('//span[@class="css-1pldt9b e1pvx6aw1" and text()="Founded"]//following-sibling::*').text
                        #founded = driver.find_element_by_xpath("//span[@class='css-1ff36h2 e1pvx6aw0']").text
                    except NoSuchElementException:
                        founded = -1

    #Type of Ownership                    
                    try:
                        #type_of_ownership = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Type"]//following-sibling::*').text
                        type_of_ownership = driver.find_element_by_xpath('//span[@class="css-1pldt9b e1pvx6aw1" and text()="Type"]//following-sibling::*').text
                    except NoSuchElementException:
                        type_of_ownership = -1

    #Industry                    
                    try:
                        #industry = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Industry"]//following-sibling::*').text
                        industry = driver.find_element_by_xpath('//span[@class="css-1pldt9b e1pvx6aw1" and text()="Industry"]//following-sibling::*').text
                    except NoSuchElementException:
                        industry = -1

    #Sector                    
                    try:
                        #sector = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Sector"]//following-sibling::*').text
                        sector = driver.find_element_by_xpath('//span[@class="css-1pldt9b e1pvx6aw1" and text()="Sector"]//following-sibling::*').text
                    except NoSuchElementException:
                        sector = -1

    #Revenue                    
                    try:
                        #revenue = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Revenue"]//following-sibling::*').text
                        revenue = driver.find_element_by_xpath('//span[@class="css-1pldt9b e1pvx6aw1" and text()="Revenue"]//following-sibling::*').text
                    except NoSuchElementException:
                        revenue = -1

    #Competitors                    
                    try:
                        #competitors = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Competitors"]//following-sibling::*').text
                        competitors = driver.find_element_by_xpath('//span[@class="css-1pldt9b e1pvx6aw1" and text()="Competitors"]//following-sibling::*').text
                    except NoSuchElementException:
                        competitors = -1

                except NoSuchElementException:  #Rarely, some job postings do not have the "Company" tab.
                    headquarters = -1
                    size = -1
                    founded = -1
                    type_of_ownership = -1
                    industry = -1
                    sector = -1
                    revenue = -1
                    competitors = -1


                if verbose:
                    print("Headquarters: {}".format(headquarters))
                    print("Size: {}".format(size))
                    print("Founded: {}".format(founded))
                    print("Type of Ownership: {}".format(type_of_ownership))
                    print("Industry: {}".format(industry))
                    print("Sector: {}".format(sector))
                    print("Revenue: {}".format(revenue))
                    print("Competitors: {}".format(competitors))
                    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

                jobs.append({"Job Title" : job_title,
                "Salary Estimate" : salary_estimate,
                "Job Description" : job_description,
                "Rating" : rating,
                "Company Name" : company_name,
                "Location" : location,
                "Headquarters" : headquarters,
                "Size" : size,
                "Founded" : founded,
                "Type of ownership" : type_of_ownership,
                "Industry" : industry,
                "Sector" : sector,
                "Revenue" : revenue,
                "Competitors" : competitors})
                #add job to jobs

            #Clicking on the "next page" button
            #try:
                #driver.find_element_by_xpath('.//li[@class="next"]//a').click()
                #driver.find_element_by_xpath('//*[@id="MainCol"]/div[2]/div/div[1]/button[7]').click()
            #except NoSuchElementException:
                #print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
                #break

    return pd.DataFrame(jobs)  #This line converts the dictionary object into a pandas DataFrame.

