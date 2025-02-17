const puppeteer = require('puppeteer');
    (async ()=>{
        const browser = await
    puppeteer.launch({ headless: false});//set headless to true to run without UI
        const page = await browser.newPage();
        // navigate to lindkedin login page
        
  // Log in
  const email = 'your_email'; // Replace with your LinkedIn email
  const password = 'your_password'; // Replace with your LinkedIn password

  await page.type('#username', email, { delay: 100 }); // Type email
  await page.type('#password', password, { delay: 100 }); // Type password
  await page.click('button[type="submit"]'); // Click login button

  // Wait for the main page to load aft
        const companyJobPage="https://www.linkedin.com/jobs/search/?currentJobId=4106957541&f_C=75752648&geoId=92000000&origin=COMPANY_PAGE_JOBS_CLUSTER_EXPANSION&originToLandingJobPostings=4106957541";
        await page.goto(companyJobPage);

        //wait for job page positing to load
        await page.waitForSelector('a[href*=/jobs/view/"]');
        console.log('Job Links:', jobLinks);

        // Save job links to a file (optional)
        const fs = require('fs');
        fs.writeFileSync('job_links.json', JSON.stringify(jobLinks, null, 2));
      
        await browser.close();
      })();
      /*  
      let jobLinks = [];

      while (true) {
        // Extract job links on the current page
        const linksOnPage = await page.evaluate(() => {
          return Array.from(document.querySelectorAll('a[href*="/jobs/view/"]')).map((job) => job.href);
        });
      
        jobLinks.push(...linksOnPage);
      
        // Check if a "Next" button exists and click it
        const nextButton = await page.$('button[aria-label="Next"]'); // Replace selector as per LinkedIn's structure
        if (nextButton) {
          await nextButton.click();
          await page.waitForTimeout(2000); // Wait for the next page to load
        } else {
          break; // No "Next" button means end of pagination
        }
      }
      
      console.log('All Job Links:', jobLinks);
      */
      
      
      
      
      