#pragma once

#include "processor/result/result_set.h"
#include "processor/result/result_set_descriptor.h"

namespace kuzu {
namespace processor {

class SourceOperator {

protected:
    explicit SourceOperator(unique_ptr<ResultSetDescriptor> resultSetDescriptor)
        : resultSetDescriptor{move(resultSetDescriptor)} {}

    shared_ptr<ResultSet> populateResultSet() {
        auto numDataChunks = resultSetDescriptor->getNumDataChunks();
        auto resultSet = make_shared<ResultSet>(numDataChunks);
        for (auto i = 0u; i < numDataChunks; ++i) {
            auto dataChunkDescriptor = resultSetDescriptor->getDataChunkDescriptor(i);
            auto dataChunk = make_shared<DataChunk>(dataChunkDescriptor->getNumValueVectors());
            if (dataChunkDescriptor->isSingleState()) {
                dataChunk->state = DataChunkState::getSingleValueDataChunkState();
            }
            resultSet->insert(i, dataChunk);
        }
        return resultSet;
    }

protected:
    unique_ptr<ResultSetDescriptor> resultSetDescriptor;
};

} // namespace processor
} // namespace kuzu
