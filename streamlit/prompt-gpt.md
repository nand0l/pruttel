Prompt:

I will deliver input in the following format:
<example>

# Module 01 - Introduction to Cloud Computing

## Slide 1: Introduction to Cloud Computing

* What is cloud computing
  + Access services on demand
  + Avoid large upfront investments
  + Provision Computing resources as needed
  + Pay only for what you use

_Notes:
Cloud computing is a transformative technology that allows users to access services on demand via the internet, eliminating the need for large upfront investments in hardware and software. It enables the provisioning of computing resources as needed, offering a flexible and scalable solution for businesses and individuals. The pay-as-you-go model ensures cost-effectiveness, as users only pay for the resources they consume. This model has revolutionized how computing resources are utilized, making technology more accessible and efficient.

Cloud computing services are offered by various providers, including Amazon Web Services (AWS), Microsoft Azure, and Google Cloud Platform (GCP). Each platform offers a range of services and solutions tailored to different needs and use cases.

For more information, visit:
* [AWS Cloud Computing](https://aws.amazon.com/what-is-cloud-computing/)
* [Microsoft Azure Cloud Computing](https://azure.microsoft.com/en-us/overview/what-is-cloud-computing/)
* [Google Cloud Platform Cloud Computing](https://cloud.google.com/learn/what-is-cloud-computing)_

## Slide 2: History and Evolution of Cloud Computing

* History and Evolution of Cloud Computing
  + How cloud computing started and its growth trajectory.

_Notes:
Cloud computing has evolved significantly since its inception. The concept of delivering computing resources over the internet can be traced back to the 1960s, with the idea of time-sharing and utility computing. However, the modern era of cloud computing began in the early 2000s, with the rise of companies like Amazon Web Services (AWS), Microsoft Azure, and Google Cloud Platform (GCP).

AWS, launched in 2006, was one of the pioneers in offering cloud computing services to the public. It started with a few basic services and has since grown into a comprehensive cloud platform with a vast array of offerings. Microsoft Azure, initially launched in 2010, has also become a major player in the cloud computing market, providing a wide range of services and solutions. GCP, introduced in 2008, has gained significant traction in recent years, particularly in areas such as big data, machine learning, and artificial intelligence.

The growth of cloud computing has been driven by factors such as the increasing demand for scalable and cost-effective computing resources, the need for agility and flexibility in business operations, and the rise of mobile and internet-connected devices. Cloud computing has revolutionized the way organizations and individuals access and utilize computing resources, enabling them to focus on their core competencies while leveraging the power and scalability of the cloud.

For more information on the history and evolution of cloud computing, visit:
* [AWS Overview](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/introduction.html)
* [Microsoft Azure History](https://azure.microsoft.com/en-us/overview/history/)
* [Google Cloud Platform History](https://cloud.google.com/about/history)_
</example>

I want to use this input (md_input) as a source for a powerpointpresentation, 
the powerpoint_source is "/pptx_source/Skillsoft_GK_Template_empty.pptx"

I want to use the md_input.titletext as the Chapter heading, 
it should be split up in 2 sections:
parts = md_input.titletext.split("-")

part1 = parts[0].strip()
part2 = parts[1].strip()
This should be used for the first slide with Layout 0, 
placeholder10 should be filled with part1, 
placeholder11 should be filled with part2.

for the next slides I want to use Layout14

the slideHeader is placeholder10
on this slide the next_level_heading ("##")as slide header
slide_header = md_input.next_level_heading.split(":")[1].strip()

The following bulletlist should be included as bulletlist,
There can be multiple levels in the bulletlist

The text sessiom starting with _Notes:
Schould be included as the notes section .in the slide.