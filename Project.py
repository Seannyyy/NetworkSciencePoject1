import Preprocessing as ps
import NetworkGraph as ng

conferenceAuthorJSON = "json/conferencesAndAuthors.json"
authorJSON = "json/authors.json"
inproceedsJSON = 'json/inproceeds.json'
dblpFilename = "DataScienceDBLP.xml"
listOfJSON = [conferenceAuthorJSON, authorJSON, inproceedsJSON]


def main ():
    # uncomment line below to preprocess dblp.xml again
    # ps.PreprocessConferencesAuthors(dblpFilename, listOfJSON)

    network = ng.Network(listOfJSON)
    # network.SaveNodesandEdges()
    network.DrawDiGraphConf(2000,2005)
    # network.DrawGraphAuth()


if __name__ == "__main__":
    main()
