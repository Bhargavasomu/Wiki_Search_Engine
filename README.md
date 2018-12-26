# Wiki_Search_Engine
Indexing and Quering on Wiki Dump of 60 GB (XML Wiki dump)

## Instructions to generate the Normal Index
The command is - 'python index.py <Path to the Data xml file>'
  
## Instructions to generate the Champions List Index
Just uncomment [this](https://github.com/Bhargavasomu/Wiki_Search_Engine/blob/8c6ef92daece62dd6c40376fafbec9aa23b78014/merge.py#L82) line and comment out [this](https://github.com/Bhargavasomu/Wiki_Search_Engine/blob/8c6ef92daece62dd6c40376fafbec9aa23b78014/merge.py#L84) line.

## Instructions to run the queries
The command is - 'python search.py <Directory Containing the indexes without />'
The top 10 relevant queries are shown and the time taken for retrieval is also shown
