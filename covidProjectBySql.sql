select * from  coviddeaths order by 2,3 desc;

select * from covidvaccinations order by 2 desc;

-- select data that we are going to
select location,date,total_cases,new_cases,population,total_deaths 
from coviddeaths 
order by 1,2;

-- looking total cases vs total deaths
-- shows likelihood of dying if you contract covid in your country
select location,date,total_cases,total_deaths,(total_deaths/total_cases)*100 as Death_percantage 
from coviddeaths 
where location like '%india%'
 order by 1,2;
 
 -- looking countries with highest infection rate compared to population
 select location,population,(total_cases) as hihestinfectioncount,max((total_cases/population))*100 as
 percentpopulationinfected 
from coviddeaths
-- where location like '%india%'
group by location,population
 order by 1,2;
 
-- looking at total cases vs population
 -- shows what percantage of popualtion got covid
 select location,date,total_cases,population,(total_cases/population)*100 as case_percantage 
from coviddeaths 
where location like '%a%'
 order by 1,2;
 
 -- Countries with Highest Death Count per Population

Select Location, MAX((Total_deaths )) as TotalDeathCount
From coviddeaths
-- Where location like '%states%'
Where continent is not null 
Group by Location
order by TotalDeathCount desc;


